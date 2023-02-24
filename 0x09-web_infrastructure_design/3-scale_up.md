![Altanother](https://raw.githubusercontent.com/B3zaleel/0x09-web_infrastructure_design/main/3-scale_up.jpg)
## Description:
---
- In this scenario, we are adding an additional server to the infrastructure and splitting the components into their own servers. We are also configuring the load-balancer as a cluster with the existing one.

- The additional server is being added to distribute the workload and ensure high availability. By splitting the components into their own servers, we are allowing for better scalability, easier maintenance, and increased fault tolerance. This allows for more efficient use of resources and easier scaling in the future.

- The load-balancer is being configured as a cluster with the existing one to ensure high availability and fault tolerance. This allows for traffic to be automatically redirected to a healthy load-balancer if one goes down, ensuring that the website remains available to users.

- In summary, the added server and split components allow for better resource utilization, scalability, and fault tolerance, while the load-balancer cluster ensures high availability and fault tolerance for the website.
