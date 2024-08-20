// ---------------------------------------------------------------------------
// Demo NodeJS Server - Hello World (HTML) Response
// ------------------------------------------------
// Note: Specify >>> 'Content-Type': 'text/html' <<<
//
// File: demo-app2.js
//
// V1 Oct'2021 dbe - initial version
// V2 Oct'2022 dbe - minor corrections in the html response data
//
// Source: Node.js Web Development - Fifth Edition (packt.com)
// ---------------------------------------------------------------------------
// required packages
import * as http from 'http';

const server = http.createServer();

server.on('request', (request, response) => {
  response.writeHead(200, {'Content-Type': 'text/html'});
  response.end(
        `<html><head><title>DEMO NodeJS App2</title></head>
        <body><h1>DEMO NodeJS App2  - Hello World HTML Response</h1>
		<h2>V2 Oct'2022 - KETE HS22</h2>
        <p><a>Hello World!</a></p>
        </body></html>`);
});

server.listen(8080, '127.0.0.1');

console.log('Server running at http://127.0.0.1:8080');