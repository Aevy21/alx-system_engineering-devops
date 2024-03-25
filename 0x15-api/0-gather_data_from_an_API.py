#!/usr/bin/python3
"""This module fetches employer information from

`jsonplaceholder` API using requests module
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"

    # Fetch user details
    response_user = requests.get(user_url)
    user_details_python = response_user.json()
    employee_name = user_details_python.get("name")

    # Fetch all tasks for the user
    todos_url = f"{todos_url}?userId={argv[1]}"
    response_tasks = requests.get(todos_url)
    all_tasks = response_tasks.json()

    # Filter completed tasks
    tasks_done = 0
    for task in all_tasks:
        # Check if task is completed
        if task.get("completed"):
            tasks_done += 1

    print(f"Employee {employee_name} is done with tasks("
              f"{tasks_done}/{len(all_tasks)}):")

    for task in all_tasks:
        if task.get("completed"):
            print(f"\t{task.get('title')}")
