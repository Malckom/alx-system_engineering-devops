
Glossary: Cybersecurity Terms & Definitions
What Is an Application Server vs. a Web Server?

Despite the contrast implied by “application server vs. web server,” on the Internet the two types of server are usually deployed together for a common purpose: fulfilling user requests for content from a website. There are no standards documents that define the properties of web servers and application servers, but let’s look at how the terms are commonly understood.

A web server‘s fundamental job is to accept and fulfill requests from clients for static content from a website (HTML pages, files, images, video, and so on). The client is almost always a browser or mobile application and the request takes the form of a Hypertext Transfer Protocol (HTTP) message, as does the web server’s response.

An application server’s fundamental job is to provide its clients with access to what is commonly called business logic, which generates dynamic content; that is, it’s code that transforms data to provide the specialized functionality offered by a business, service, or application. An application server’s clients are often applications themselves, and can include web servers and other application servers. Communication between the application server and its clients might take the form of HTTP messages, but that is not required as it is for communication between web servers and their clients. Many other protocols are popular, including the variants of CGI.
How Do Application Servers and Web Servers Work Together?

In a typical deployment, a website that provides both static and dynamically generated content runs web servers for the static content and application servers to generate content dynamically. A reverse proxy and load balancer sit in front of one or more web servers and one or more web application servers to route traffic to the appropriate server, first based on the type of content requested and then based on the configured load-balancing algorithm. Most load balancer programs are also reverse proxy servers, which simplifies web application server architecture.
Why the Question?

Why is it a question whether something is an application server vs. a web server? It’s largely due to how the design and use of the two types of servers has increasingly come to overlap as the demands on websites have grown. Many popular applications act as both web servers and application servers (think Apache HTTP Server, Express, Hapi, and Koa).

Another overlap is that some web application servers use HTTP as their communication protocol. Similarly, some web servers end up looking like application servers because they have built-in modules and functionality that natively support popular languages like PHP, or proxy and translate requests from HTTP into the protocol (such as FastCGI) used by the application.
How Can NGINX Plus Help?

NGINX Plus and NGINX are the best-in-class load‑balancing solutions used by high‑traffic websites such as Dropbox, Netflix, and Zynga. More than 350 million websites worldwide rely on NGINX Plus and NGINX Open Source to deliver their content quickly, reliably, and securely.

NGINX Plus is an extremely efficient reverse proxy and load balancer when deployed in front of web and application servers, with translation modules for several types of application server including FastCGI and SCGI. NGINX Plus combines multiple functions – including web serving, advanced load balancing, caching, management and monitoring, and request routing – all in one flexible, cost-effective solution for delivering static and dynamic content in a fast and reliable manner that boosts customer satisfaction and revenue. It’s the complete application delivery platform essential for today’s high-performance web sites.
