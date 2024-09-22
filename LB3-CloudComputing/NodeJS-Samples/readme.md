## NodeJS Sample Applications

> ##### last update 16.11.23 - dbe  node.js sample scripts added

### What is Node.JS?  
[Node.js](https://nodejs.org/en) is an **open-source and cross-platform JavaScript runtime environment**. It is a popular tool for almost any kind of project! Node.js runs the **V8 JavaScript engine**, the core of Google Chrome, outside of the browser. This allows Node.js to be very performant.

A Node.js app runs in a single process, without creating a new thread for every request. Node.js provides a set of asynchronous I/O primitives in its standard library that prevent JavaScript code from blocking and generally, libraries in Node.js are written using non-blocking paradigms, making blocking behavior the exception rather than the norm.

When Node.js performs an I/O operation, like reading from the network, accessing a database or the filesystem, instead of blocking the thread and wasting CPU cycles waiting, Node.js will resume the operations when the response comes back.

This allows Node.js to handle thousands of concurrent connections with a single server without introducing the burden of managing thread concurrency, which could be a significant source of bugs.   


### Example Node.js Scripts   
+ **demo-chat-app3.js**  
Multi-user chat room application. Use the chat service via browser and the url   
``` http://<server-ip-address>:3000 ```

+ **demo-encode1.js**  
Symmetric string encoding/decoding service, using an internal cipher. Use the encoding service via browser and the url  
``` http://<server-ip-address>:7777?encode=xxx ```, where xxx is the string to encode  

+ **demo-hashingMD5.js**  
MD5 hashing service. Use the encoding service via browser and the url  
``` http://<server-ip-address>:7777?md5=xxx ```,  where xxx is the string to hash 

+ **demo-server1.js**  
Hello World example web (http/html) server. Use the encoding service via browser and the url  
``` http://<server-ip-address>:8080 ```


### Links:
+ [9 Examples of successful Node.js apps](https://www.masterborn.com/blog/Why_use_nodejs_9_examples_of_node_apps)
+ [Tutorialspoint](https://www.tutorialspoint.com/nodejs/index.htm) for a easy learning tutorial
+ [Node.js Video Tutorial](https://youtu.be/LAUi8pPlcUM?si=ccitXniIqRSz8DGP&t=52)

---  
Source:   
+ see [Github](https://github.com/nodejs) for the official open source code and documentation repository   
---  

![image](https://github.com/sawubona-repo/KETE-HS23-WORK/assets/52699611/4acbbb73-6e56-4f08-b3d9-00a926a1724b)


