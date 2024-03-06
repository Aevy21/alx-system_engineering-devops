# Debugging Web Stack

This README provides an overview of common concepts and commands used to debug a web stack, focusing on troubleshooting issues related to Nginx.

## Concepts

### Nginx Configuration Files
- **nginx.conf**: Main configuration file for Nginx, contains global settings.
- **sites-available**: Directory where individual site configuration files are stored.
- **sites-enabled**: Directory containing symbolic links to configuration files in `sites-available`. Nginx reads configurations from this directory.

### Ports and Processes
- **Ports**: Numeric identifiers used by networking protocols to distinguish between different services running on the same host.
- **Processes**: Instances of running programs on a computer system.

## Commands

### Check Nginx Processes
To check if Nginx processes are running:
```bash
pgrep nginx
```

### Check Listening Ports
To list all listening ports and associated processes:
```bash
netstat -tuln
```

### Remove Default Nginx Configuration
To remove the default Nginx configuration file from the enabled sites directory:
```bash
rm /etc/nginx/sites-enabled/default
```

### Create Symbolic Link for Configuration
To create a symbolic link to a Nginx configuration file in the enabled sites directory:
```bash
ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
```

### Restart Nginx Service
To restart the Nginx service:
```bash
service nginx restart
```

## Conclusion
Debugging a web stack often involves checking for running processes, examining listening ports, and managing configuration files. By understanding these concepts and using appropriate commands, you can effectively troubleshoot issues with your web server setup.
