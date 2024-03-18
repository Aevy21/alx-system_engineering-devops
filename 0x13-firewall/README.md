# Firewall Setup using UFW (Uncomplicated Firewall)

## Overview
This README provides instructions on setting up a firewall using UFW (Uncomplicated Firewall) on a Linux server to allow specific incoming TCP ports while blocking all other traffic. This setup ensures improved security by restricting access to only essential services.

## Requirements
- Linux server (e.g., Ubuntu, Debian) with UFW installed
- Administrative privileges (sudo or root access)

## Installation
If UFW is not already installed on your server, you can install it using the following commands:
```bash
sudo apt update
sudo apt install ufw
```

## Configuration Steps
1. **Define Default Policies**:
   Set default policies to deny incoming and allow outgoing traffic:
   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   ```

2. **Allow Specific Ports**:
   Allow incoming traffic on specific TCP ports (e.g., SSH, HTTPS, HTTP):
   ```bash
   sudo ufw allow 22/tcp  # SSH
   sudo ufw allow 443/tcp # HTTPS
   sudo ufw allow 80/tcp  # HTTP
   ```

3. **Enable UFW**:
   Enable UFW to activate the configured firewall rules:
   ```bash
   sudo ufw enable
   ```

4. **Check Status**:
   Verify the status of UFW to ensure that rules are applied correctly:
   ```bash
   sudo ufw status
   ```

## Exiting Server Safely
To exit the server safely while ensuring port 22 (SSH) remains unblocked, run the following command before exiting:
```bash
sudo ufw allow 22/tcp
```

## Additional Notes
- **Logging**: UFW can log blocked connections to `/var/log/ufw.log` for monitoring purposes.
- **Custom Rules**: Advanced users can create custom rules using UFW to meet specific requirements.

## Example Usage
```bash
# Install UFW (if not already installed)
sudo apt update
sudo apt install ufw

# Configure UFW rules
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp

# Enable UFW
sudo ufw enable

# Check UFW status
sudo ufw status
```

## Resources
- [UFW Documentation](https://help.ubuntu.com/community/UFW)
- [DigitalOcean UFW Essentials](https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands)

