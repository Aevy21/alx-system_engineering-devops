# 0x0F. Load balancer
# SCP and Nginx Setup Script

## Overview
This script automates the setup of SCP file transfer and Nginx configuration on Ubuntu servers. It facilitates the secure transfer of files from a client machine to a server using SCP and configures Nginx for redirection and default error pages.

## Features
- Transfer files securely from client to server using SCP.
- Configure Nginx server for redirection and default error pages.
- Support for multiple server names or IP addresses in Nginx configuration.

## Usage
1. Ensure the script is executed with appropriate permissions.
2. Run the script with the following parameters:
   ```
   ./scp_and_nginx_setup.sh PATH_TO_FILE SERVER_IP USERNAME PATH_TO_SSH_KEY
   ```
   Replace `PATH_TO_FILE`, `SERVER_IP`, `USERNAME`, and `PATH_TO_SSH_KEY` with actual values.
   
## SCP Transfer
The script securely transfers a file from the client to the server using SCP. It verifies the number of arguments provided and performs the transfer using SSH key authentication.

## Nginx Configuration
The script configures the Nginx server for redirection and default error pages:
- It installs Nginx, creates a backup of the default configuration, and opens the necessary firewall ports.
- The default index page is set to display "Hello World!" for testing purposes.
- Redirection rules are added to redirect specific URLs to external resources.
- Custom error pages are created and configured to handle HTTP 404 errors.

## Load Balancer Configuration
For load balancing across multiple servers, you can use a load balancer such as NGINX Plus or HAProxy. Here's a basic setup:

1. Install and configure the load balancer software on a separate server.
2. Add the IP addresses or domain names of your servers to the load balancer configuration.
3. Configure the load balancer to distribute incoming traffic evenly across the servers.
4. Monitor the load balancer for performance and scalability.

## Note
- Ensure that the script is executed with appropriate permissions and that the provided file paths and server details are accurate.
- Customize the Nginx configuration according to your specific requirements and server setup.
- For production environments, consider additional security measures such as SSL/TLS encryption and access control.

---.
