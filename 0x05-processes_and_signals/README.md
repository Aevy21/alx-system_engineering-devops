# Linux Process and Signal Management

## 1. Processes and Signals

### Definition of Processes:
In Linux, a process is an instance of a running program, consisting of code, data, and resources.

### Definition of Signals:
Signals are software interrupts used for inter-process communication and management.

### Table of State Codes:

| State Code | Description            |
|------------|------------------------|
| R          | Running                |
| S          | Sleeping               |
| D          | Disk Sleep (uninterruptible)|
| Z          | Zombie                 |
| T          | Traced or Stopped      |
| ...

## 2. Getty Process

A Getty process manages terminal logins, facilitating user login to the system.

## 3. Commonly Used Process Management Commands

- **PS Command Trio:**
  - `ps `: Customized process information.
  - `ps -ef`: Detailed process list.

- **Killer Commands:**
  - `kill`: Terminate a process.
  - `kill -9`: Forcefully terminate.

- **PS Grep:**
  - `ps aux | grep <process_name>`: Display info about a specific process.

- **Nice Command:**
  - `nice`: Set/change process priority.

- **Top Command:**
  - `top`: Display real-time system stats and process list.

- **Trap Command:**
  - `trap 'command' signal`: Execute command on signal reception.

## 4. PS Command Features

- **Sorting:**
  - `ps aux --sort=-%cpu`: Sort by CPU usage.
  
- **Tree Visualization:**
  - `pstree`: Display process hierarchy.

- **Filtering:**
  - `ps aux | grep <process_name>`: Filter processes by name.

## 5. Signals

### Muscible Signals:
- **SIGTERM (15):** Gracefully terminate.
- **SIGHUP (1):** Hangup signal, often used to restart.

### Non-Muscible Signals:
- **SIGKILL (9):** Forceful termination.
- **SIGSTOP (19):** Stop a process.

## 6. Trap Command

The `trap` command catches signals and executes specified actions.

Example:
```bash
trap 'echo "Ctrl+C is disabled."' SIGINT
```

## 7. PS Command Trio and Additional Features

- **Sorting by Memory Usage:**
  - `ps aux --sort=-%mem`

- **Filtering by User:**
  - `ps -u <username>`

- **Visualization using Tree:**
  - `pstree -p`

- **Sorting by Start Time:**
  - `ps -eo pid,cmd,lstart --sort=start`

## 8. Process Priority (Nice Command)

Example:
```bash
nice -n 10 command
```

## 9. Process Tree Visualization with pstree

Example:
```bash
pstree -c
```

## 10. Advanced PS Command Sorting

Example:
```bash
ps aux --sort=-%mem,%cpu
```

## 11. Top Command for Real-time Monitoring

Example:
```bash
top
```

## 12. Filtering Processes with PS

Example:
```bash
ps aux | grep <username>
```

## 13. Sorting PS Output by Multiple Criteria

Example:
```bash
ps aux --sort=-%mem,%cpu
```

## 14. Additional Signal Handling

- **SIGCHLD (17):** Sent when a child process exits.
- **SIGWINCH (28):** Sent when terminal window size changes.

## 15. Muscible and Non-Muscible Signal Examples

- **Muscible (SIGTERM):**
  ```bash
  kill -15 <pid>
  ```

- **Non-Muscible (SIGKILL):**
  ```bash
  kill -9 <pid>
  ``
