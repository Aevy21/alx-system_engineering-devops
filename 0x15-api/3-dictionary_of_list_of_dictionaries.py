#!/usr/bin/python3
"""This module fetches employer information from
`jsonplaceholder` API using requests module
and exports tasks in JSON format
"""

import json
import os
import requests
from sys import argv


def export_tasks_to_json(user_id, tasks):
    # Prepare the tasks data in the required format
    formatted_tasks = []
    for task in tasks:
        formatted_task = {
            "username": user_id,
            "task": task["title"],
            "completed": task["completed"]}
        formatted_tasks.append(formatted_task)

    employees_task = {user_id: formatted_tasks}

    file_name = "todo_all_employees.json"
    if not os.path.exists(file_name):
        with open(file_name, "w") as json_file:
            json.dump({}, json_file)

    with open(file_name, "r") as json_file:
        all_employees_tasks = json.load(json_file)

    all_employees_tasks.update(employees_task)

    with open(file_name, "w") as json_file:
        json.dump(all_employees_tasks, json_file, indent=4)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script_name.py <user_id>")
        exit(1)

    user_id = argv[1]
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response_user = requests.get(user_url)
    if response_user.status_code != 200:
        print(f"Error fetching user details for User ID: {user_id}")
        exit(1)

    user_details = response_user.json()
    employee_name = user_details.get("name")

    response_tasks = requests.get(todos_url)
    if response_tasks.status_code != 200:
        print(f"Error fetching tasks for User ID: {user_id}")
        exit(1)

    tasks_data = response_tasks.json()
    export_tasks_to_json(user_id, tasks_data)

    print(f"Tasks exported to todo_all_employees.json for User ID: {user_id}")
