![Screenshot](https://raw.githubusercontent.com/B3zaleel/0x09-web_infrastructure_design/main/0-simple_web_stack.jpg
)
---
# Description
---
This is a simple web infrastructure that hosts a website that is reachable via www.foobar.com. There are no firewalls or SSL certificates for protecting the server's network. Each component (database, application server) has to share the resources (CPU, RAM, and SSD) provided by the server.
---

# SPECIFICS ABOUT THIS INFRASTRUCTURE
---

## Server:
A server is a computer system that is responsible for processing requests and serving information to clients over a network. It can be a physical or virtual machine that hosts one or more applications.

## Domain name:
A domain name is a unique identifier that is used to locate a website on the internet. It provides a human-readable name for the IP address of the server that hosts the website.

## DNS record:
The www record is a subdomain that is used to identify the web server that hosts the website. It is an A record that points to the IP address of the server.

## Web server:
The web server is responsible for serving web pages to clients over the HTTP or HTTPS protocol. In this case, we will use Nginx as our web server.

## Application server:
The application server is responsible for executing the code that generates the dynamic content of the website. We will use PHP-FPM as our application server.

## Application files:
The application files contain the code that generates the dynamic content of the website. It includes HTML, CSS, JavaScript, and PHP files.

## Database:
The database is responsible for storing and retrieving data that is used by the application. We will use MySQL as our database server.

## Communication:
The server uses the HTTP protocol to communicate with the computer of the user requesting the website. When the user types www.foobar.com into their web browser, it sends an HTTP request to the server, which responds with the web pages that make up the website.

# Issues with this infrastructure:

- Single Point of Failure (SPOF): If the server goes down, the website becomes inaccessible. To avoid this, we can set up a load balancer and add more servers to the infrastructure.

- Downtime during maintenance: When deploying new code, the web server needs to be restarted, which causes downtime for the website. To minimize this, we can use rolling deployments that update the website one server at a time.
- Scalability: This infrastructure cannot handle high levels of incoming traffic. To scale the infrastructure, we need to add more servers and use a load balancer to distribute the traffic between them.
