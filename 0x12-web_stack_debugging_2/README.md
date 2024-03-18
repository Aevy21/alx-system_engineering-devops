# Web Stack Debugging and User Management

## Introduction
This README provides guidance on web stack debugging and user management in a Linux environment. It covers common issues related to user privileges, adding new users with specific privileges, and best practices for managing user permissions.

## Debugging Web Stack Issues
When dealing with web stack issues, especially those related to user permissions, it's essential to understand the following concepts:

1. **Root User (`root`):** The root user has full administrative privileges on a Linux system. It can perform any action and access any file on the system.

2. **Regular Users:** Regular users have limited privileges compared to the root user. They can perform actions based on their assigned permissions.

## User Management
### Adding a New User
To add a new user to the system with specific privileges, follow these steps:

1. **Log in as Root:** Ensure you are logged in as the root user or have sudo privileges.

2. **Add User:** Use the `adduser` command to add a new user. Replace `<username>` with the desired username.
   ```bash
   sudo adduser <username>
   ```

3. **Set Password:** Set a password for the new user when prompted.

4. **Grant Privileges:** Assign specific privileges to the user as needed. For example, to grant sudo (administrative) privileges:
   ```bash
   sudo usermod -aG sudo <username>
   ```

5. **Verify User Addition:** Verify that the user is added correctly by switching to the new user and checking permissions.
   ```bash
   su - <username>
   ```

### Example Scenario
Let's consider an example scenario where we add a user named `webadmin` with sudo privileges:

```bash
sudo adduser webadmin
sudo usermod -aG sudo webadmin
su - webadmin
```

## Additional Tips
- **User Groups:** Utilize user groups (`sudo`, `www-data`, etc.) to manage permissions effectively.
- **File Permissions:** Use `chmod` and `chown` commands to modify file permissions and ownership.

## Conclusion
By following the guidelines in this README, you can effectively debug web stack issues related to user permissions and manage users with specific privileges on your Linux 
