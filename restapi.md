# REST API

> REST - Representational State Transfer

 - Uses HTTP protocol for implementation.
 - These services are lightweight, provide maintainabiliy, scalability, support communication among multiple applications that are developed using different programming languages.
 - Provide means to access resource present at the server required by the client using the request, response architecture

Contents
 - [REST Resource](#rest-resource-back-to-top)
 - [Statelessness](#statelessness-in-rest-back-to-top)
 - [Status codes](#status-code)
 - [HTTP methods](#http-methods-back-to-top)

---

### REST Resource <a href="#" style="float:right;font-size:.7em;">Back to top</a>
Every content in REST architecture is considered to be a resource.\
The resource is analogous to `object` in `OOP` concepts i.e. it can be HTML pages, images, text files, XML, json, or any other dynamic data.

---

### Statelessness in REST <a href="#" style="float:right;font-size:.7em;">Back to top</a>

The REST architecture is designed in such a way that the client state is not maintained on the server.\
The context is provided by the client itslef in the request using which the server is able to process the request.\
The session on the server is identified by the session identifier (cookie) sent by the client. 

---

### Status code <a href="#" style="float:right;font-size:.7em;">Back to top</a>

 - 1xx - represents informational responses
 - 2xx - represents successful responses
 - 3xx - represents redirects
 - 4xx - represents client side error
 - 5xx - represents server side error

---

### HTTP Methods <a href="#" style="float:right;font-size:.7em;">Back to top</a>

 - Get
 - Put
 - Post
 - Delete
 - Patch
 - Options

Get, Head, and Option are safe and  idempotent\
Put and Delete are only idempotent\
Post and Patch are netiher 

---

