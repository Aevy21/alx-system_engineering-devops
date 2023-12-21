# README: SSH Key Generation and Bash Scripting

## SSH Key Generation:

### Steps to Generate SSH Keys:

1. Open a terminal on your local machine.

2. Run the following command to generate an SSH key pair:
   ```bash
   ssh-keygen -t rsa -b 2048
   ```

3. You will be prompted to enter a file to save the key. Press Enter to use the default location (`~/.ssh/id_rsa`) or specify a custom path.

4. Optionally, provide a passphrase for additional security.

5. Your SSH key pair will be generated, with the private key stored locally and the public key (`id_rsa.pub`) available for sharing.

### Viewing Private and Public Keys:

- To view the private key:
  ```bash
  cat ~/.ssh/id_rsa
  ```

- To view the public key:
  ```bash
  cat ~/.ssh/id_rsa.pub
  ```

## Passphrase:

A passphrase is an additional layer of security for your private key. It's like a password associated with your key. You can set a passphrase during key generation or later using the `ssh-keygen -p` command.

## Bash Shell Scripting:

### Loops:

- **While Loop:**
  ```bash
  while [ condition ]; do
    # commands
  done
  ```

- **Until Loop:**
  ```bash
  until [ condition ]; do
    # commands
  done
  ```

- **For Loop:**
  ```bash
  for item in list; do
    # commands
  done
  ```

### Conditional Statements:

- **If, Else, Elif:**
  ```bash
  if [ condition ]; then
    # commands
  elif [ condition ]; then
    # commands
  else
    # commands
  fi
  ```

- **Case Statement:**
  ```bash
  case $variable in
    pattern1)
      # commands
      ;;
    pattern2)
      # commands
      ;;
    *)
      # default case
      ;;
  esac
  ```

### Cut Command:

To extract specific columns or fields from a file:
```bash
cut -d delimiter -f fields input_file
```

### File and Comparison Operators:

- **File Operators:**
  - `-e file`: True if file exists.
  - `-f file`: True if file exists and is a regular file.
  - `-d file`: True if file exists and is a directory.

- **Comparison Operators:**
  - `==`: Equal to
  - `!=`: Not equal to
  - `-eq`: Equal to (numeric comparison)
  - `-ne`: Not equal to (numeric comparison)
  - `-lt`, `-le`, `-gt`, `-ge`: Less than, Less than or equal to, Greater than, Greater than or equal to.


