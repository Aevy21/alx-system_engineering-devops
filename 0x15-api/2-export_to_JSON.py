#!/usr/bin/python3
"""This module fetches employer information from
`jsonplaceholder` API using requests module
and exports tasks in JSON format
"""

import json
import requests
from sys import argv


def export_tasks_to_json(user_id, tasks):
    user_tasks = {
        user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_details_python.get("username")
        } for task in tasks]
    }

    file_name = f"{user_id}.json"
    with open(file_name, "w") as json_file:
        json.dump(user_tasks, json_file, indent=4)


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

    # Initialize completed tasks count
    completed_tasks_count = 0

    for task in all_tasks:
        # Check if task is completed
        if task.get("completed"):
            completed_tasks_count += 1

    # Export tasks to JSON
    export_tasks_to_json(argv[1], all_tasks)
