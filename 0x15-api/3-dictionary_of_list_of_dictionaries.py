#!/usr/bin/python3
"""This module fetches employer information from
`jsonplaceholder` API using requests module
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]  # Assuming user_id is passed as a command-line argument
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    # Fetch user details
    response_user = requests.get(user_url)
    user_details_python = response_user.json()
    employee_name = user_details_python.get("name")
    
    # Fetch all tasks for the user
    todos_url = f"{todos_url}?userId={user_id}"
    response_tasks = requests.get(todos_url)
    all_tasks = response_tasks.json()
    
    # Initialize dictionary to store tasks for all employees
    all_employees_tasks = {}

    # Filter completed tasks for the user
    tasks_done = []
    for task in all_tasks:
        task_details = {
            "username": employee_name,
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        tasks_done.append(task_details)

    # Add tasks to the dictionary for the corresponding user_id
    all_employees_tasks[user_id] = tasks_done

    # Write data to JSON file
    output_file = "todo_all_employees.json"
    with open(output_file, "w") as json_file:
        json.dump(all_employees_tasks, json_file, indent=4)

    print(f"Data exported to {output_file} successfully.")
