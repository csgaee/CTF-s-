const { Web3 } = require("web3");
const fs = require("fs");

const web3 = new Web3("https://bsc-testnet-rpc.publicnode.com");
const contractAddress = "0x9223f0630c598a200f99c5d4746531d10319a569";
const filePath = "decoded_output.txt";

async function callContractFunction(inputString) {
    try {
        // First method call - encoding string parameter
        const methodId = "0x5684cff5";
        const encodedData = methodId + web3.eth.abi.encodeParameters(["string"], [inputString]).slice(2);
        console.log("Encoded Data for first call:", encodedData);

        const result = await web3.eth.call({
            to: contractAddress,
            data: encodedData
        });
        console.log("Result from First Call:", result);

        // Decode the string result
        const largeString = web3.eth.abi.decodeParameter("string", result);
        console.log("Decoded Large String:", largeString);

        // Decode base64 to get the target address
        const targetAddress = Buffer.from(largeString, "base64").toString("utf-8");
        console.log("Target Address:", targetAddress);

        // Save the address to file
        fs.writeFileSync(filePath, "$address = " + targetAddress + "\n");

        // Second method call - encoding address parameter
        const newMethodId = "0x5c880fcb";
        const blockNumber = 43152014;
        const newEncodedData = newMethodId + web3.eth.abi.encodeParameters(["address"], [targetAddress]).slice(2);
        console.log("Encoded Data for second call:", newEncodedData);

        const newData = await web3.eth.call({
            to: contractAddress,
            data: newEncodedData
        }, blockNumber);
        console.log("Result from Second Call:", newData);

        // Decode the string result from the second call
        const decodedData = web3.eth.abi.decodeParameter("string", newData);
        console.log("Decoded Data from Second Call:", decodedData);

        // Decode base64 data to get the final output
        const base64DecodedData = Buffer.from(decodedData, "base64").toString("utf-8");
        console.log("Decoded Base64 Data:", base64DecodedData);

        // Save the final decoded data to file
        fs.writeFileSync(filePath, base64DecodedData);
        console.log(`Saved decoded data to: ${filePath}`);
    } catch (error) {
        console.error("Error calling contract function:", error);
    }
}

// Input string for the contract function
const inputString = "giV3_M3_p4yL04d!";
callContractFunction(inputString);
