// ---------------------------------------------------------------------------
// Demo NodeJS Server - String HASHING Service
// --------------------------------------------
// Usage http://127.0.0.1:7777?md5="xxx" where xxx is the string to hash with MD5
// Incl. Server Side Request/Originator Logging
// 
// Note: delete/deactivate <"type": "module"> in the package.json config file
//
// File: demo-hashingMD5.js
//
// V1 Nov'2021 dbe - initial version, KETE-HS21, based on fibonacci.js example
//
// Source: Node.js Web Development - Fifth Edition (packt.com)
// ---------------------------------------------------------------------------
// required packages
var http = require('http');
var url  = require('url');
var crypto = require('crypto');

//Define the MD5 hashing function to encode a string
const hashingMD5 = exports.hashingMD5 = function(str) {
    return crypto.createHash('md5').update(str).digest('hex');
}

//Define the SHA256 hashing function to encode a string
const hashingSHA256 = exports.hashingSHA256 = function(str) {
    return crypto.createHash('sha256').update(str).digest('hex');
}

// ------------------------------------------------------------------------------
// Setup a http server acting on the request parameter
// Usage http://127.0.0.1:7777?md5="xxx" where xxx is the string to hash
// ------------------------------------------------------------------------------
http.createServer(function (request, response) {
  var urlP = url.parse(request.url, true);
  var xMD5;
  var xSHA256;
    
  response.writeHead(200, {'Content-Type': 'text/plain'});
  
  if (urlP.query['md5']) {
    xMD5 = hashingMD5(urlP.query['md5']);
    response.end('MD5 Hashed String '+ urlP.query['md5'] +' = '+ xMD5);
	console.log('-- md5 hashing request: string > '+ urlP.query['md5']);
  } else {
	   if (urlP.query['sha256']) {
			xSHA256 = hashingSHA256(urlP.query['sha256']);
			response.end('SHA256 Hashed String '+ urlP.query['sha256'] +' = '+ xSHA256);
			console.log('-- sha256 hashing request: string > '+ urlP.query['sha256']);
		} else {
			response.end('USAGE: http://127.0.0.1:7777?key=xxx where xxx is the string to hash and key = md5 or sha256');
		}
  }
}).listen(7777, );
console.log('Server listening on port 7777');
