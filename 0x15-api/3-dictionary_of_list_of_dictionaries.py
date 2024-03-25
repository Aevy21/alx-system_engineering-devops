#!/usr/bin/python3
"""This module fetches employer information from
`jsonplaceholder` API using requests module
"""
import json
import requests

if __name__ == "__main__":
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"

    # Fetch user details
    response_users = requests.get(user_url)
    user_details_python = response_users.json()

    # Extract user IDs and names
    user_id_name = [(str(user.get("id")),
                     user.get("username")) for user in user_details_python]

    task_dict = {}
    for user_id, username in user_id_name:
        todos_url_user = f"{todos_url}?userId={user_id}"
        response_tasks = requests.get(todos_url_user)
        all_tasks = response_tasks.json()

        tasks_list = [{"username": username,
                       "task": task.get("title"),
                       "completed": task.get("completed")
                       } for task in all_tasks]

        task_dict[user_id] = tasks_list

        # Write data to JSON file
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(task_dict, json_file, indent=4)
