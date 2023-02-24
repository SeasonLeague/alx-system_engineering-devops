![Sreenshot](https://raw.githubusercontent.com/B3zaleel/0x09-web_infrastructure_design/main/1-distributed_web_infrastructure.jpg
)

# Description
---

### Server 1:
This server will act as the primary web server and will host the website files. We will use Nginx as the web server and PHP-FPM as the application server.

### Server 2:
This server will act as a replica of Server 1 and will also host the website files. We will use Nginx as the web server and PHP-FPM as the application server.

### Server 3:
This server will act as the load balancer and will distribute incoming traffic between Server 1 and Server 2. We will use HAproxy as the load balancer.

### Application files:
The application files will contain the code that generates the dynamic content of the website. It includes HTML, CSS, JavaScript, and PHP files.

### Database:
We will use a MySQL database cluster with a Primary-Replica (Master-Slave) configuration to store and retrieve data used by the application.
---

### Why we are adding each element:
We are adding the additional servers to improve the performance, scalability, and availability of the website. The load balancer will distribute incoming traffic between the two web servers, allowing us to handle more requests and reducing the risk of downtime due to a single server failure. The database cluster will ensure that we can handle high levels of concurrent reads and writes and provide fault-tolerance in case of a database server failure.

### Load balancer distribution algorithm:
We will configure HAproxy with a round-robin distribution algorithm. This means that incoming requests will be evenly distributed between the two web servers in a rotating sequence.

### Active-Active or Active-Passive setup:
The load balancer is enabling an Active-Active setup, meaning that both web servers are actively serving requests and are equally responsible for handling incoming traffic.

### How a database Primary-Replica cluster works:
In a Primary-Replica (Master-Slave) configuration, the Primary node is the main database server that receives all write requests and replicates the changes to the Replica nodes. The Replica nodes are read-only copies of the Primary node that can be used to handle read requests and provide fault-tolerance in case the Primary node fails.

### Difference between the Primary node and the Replica node in regard to the application:
The Primary node is responsible for handling all write requests and making sure that the data is consistent across all nodes in the cluster. The Replica nodes are read-only copies that can be used to handle read requests but cannot modify the data. As a result, the application needs to be configured to send write requests to the Primary node and read requests to any node in the cluster.

# Issues with this infrastructure:

- Single Point of Failure (SPOF): The load balancer is a SPOF. If it fails, incoming traffic will not be distributed between the web servers, and the website will become unavailable. To mitigate this, we can add another load balancer and configure them in a High Availability (HA) setup.

- Security issues: The infrastructure is lacking a firewall and HTTPS encryption, making it vulnerable to cyber-attacks and data breaches. We can add a firewall and configure HTTPS encryption to improve security.

- No monitoring: Without monitoring, it's difficult to detect and troubleshoot issues that affect the website's performance and availability. We can add a monitoring solution to monitor the infrastructure's health and alert us in case of any issues.
