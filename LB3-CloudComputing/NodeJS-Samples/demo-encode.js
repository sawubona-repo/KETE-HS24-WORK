// ---------------------------------------------------------------------------
// Demo NodeJS Server - String ENCODING Service
// --------------------------------------------
// Usage http://<server-ip-address>:7777?encode="xxx" where xxx is the string to encode
// Incl. Server Side Request/Originator Logging
// 
// Note: delete/deactivate <"type": "module"> in the package.json config file
//
// File: demo-encode1.js
//
// V1 Oct'2021 dbe - initial version, KETE-HS21, based on fibonacci.js example
// V2 Oct'2022 dbe - minor corrections for KETE-HS22
//
// Source: Node.js Web Development - Fifth Edition (packt.com)
// ---------------------------------------------------------------------------
// required packages
var http = require('http');
var url  = require('url');

// local functions, objects
const cipher = salt => {
    const textToChars = text => text.split('').map(c => c.charCodeAt(0));
    const byteHex = n => ("0" + Number(n).toString(16)).substr(-2);
    const applySaltToChar = code => textToChars(salt).reduce((a,b) => a ^ b, code);

    return text => text.split('')
        .map(textToChars)
        .map(applySaltToChar)
        .map(byteHex)
        .join('');
}

// To create a (symmetric) cipher and decypher define a key string
const myCipher = cipher('mySecretKey2022')

//Then define the ENCRYPTION function to cipher a string
const encryption = exports.encryption = function(str) {
    return myCipher(str);
}

// ------------------------------------------------------------------------------
// Setup a http server acting on the 'encode' request parameter
// Usage http://<server-ip-address>:7777?encode="xxx" where xxx is the string to encode
// ------------------------------------------------------------------------------
http.createServer(function (request, response) {
  var urlP = url.parse(request.url, true);
  var xEncode;
    
  response.writeHead(200, {'Content-Type': 'text/plain'});
  
  if (urlP.query['encode']) {
    xEncode = encryption(urlP.query['encode']);
    response.end('Encoded String '+ urlP.query['encode'] +' = '+ xEncode);
	console.log('-- encoding request: string > '+ urlP.query['encode']);
  } else {
	response.end('USAGE: http://<server-ip-address>:7777?encode=xxx where xxx is the string to encode');
  }
}).listen(7777, );
console.log('Server running at port 7777');
