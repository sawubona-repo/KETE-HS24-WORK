// ------------------------------------------------------------------------
// Demo NodeJS Server - Hello World (HTML) Response
// ------------------------------------------------
// Note: Specify >>> 'Content-Type': 'text/html' <<<
//
// File: demo-app1.js
//
// V1 Oct'2021 dbe - initial version
// V2 Oct'2022 dbe - minor corrections in the html response data
// V3 Sep'2024 dbe - replace import by require
//
// Source: Node.js Web Development - Fifth Edition (packt.com)
// ---------------------------------------------------------------------------
// required packages

var http = require('http');
var server = http.createServer();

server.on('request', (request, response) => {
  response.writeHead(200, {'Content-Type': 'text/html'});
  response.end(
        `<html><head><title>DEMO NodeJS App</title></head>
        <body><h1>DEMO NodeJS App1  - Hello World HTML Response</h1>
		<h2>V3 Sept'2024 - KETE HS24</h2>
        <p><a>Hi Folks!</a></p>
        </body></html>`);
});

server.listen(8080, );

console.log('Server listening on port 8080');