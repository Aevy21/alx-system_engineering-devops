#!/usr/bin/python3
"""This module fetches employer information from
`jsonplaceholder` API using requests module
and exports tasks in JSON format
"""

import json
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

        file_name = f"todo_all_employees.json"
        with open(file_name, "w") as json_file:
            json.dump(employees_task, json_file, indent=4)

            if __name__ == "__main__":
                todos_url = "https://jsonplaceholder.typicode.com/todos"
                user_id = argv[1]
                user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

                # Fetch user details
                response_user = requests.get(user_url)
                user_details_python = response_user.json()
                employee_name = user_details_python.get("name")

                # Fetch all tasks for the user
                todos_url = f"{todos_url}?userId={user_id}"
                response_tasks = requests.get(todos_url)
                all_tasks = response_tasks.json()

                # Export tasks to JSON
                export_tasks_to_json(user_id, all_tasks)

                print(
                    f"Tasks exported to todo_all_employees.json for User ID: {user_id}")
