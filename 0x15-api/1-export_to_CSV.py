#!/usr/bin/python3
"""This module fetches employer information from
`jsonplaceholder` API using requests module
and exports tasks data in CSV format
"""

import json
import requests
from sys import argv
import csv

if __name__ == "__main__":
    user_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user details
    response_user = requests.get(user_url)
    user_details_python = response_user.json()
    employee_name = user_details_python.get("name")
    user_id = argv[1]

    # Fetch all tasks for the user
    todos_url = f"{todos_url}?userId={argv[1]}"
    response_tasks = requests.get(todos_url)
    all_tasks = response_tasks.json()

    # Filter completed tasks
    tasks_done = 0
    # List to store task data
    task_data = []
    for task in all_tasks:
        # Check if task is completed
        if task.get("completed"):
            tasks_done += 1
            task_data.append(
                [user_id, employee_name, "Completed", task.get('title')])
        else:
            task_data.append(
                [user_id, employee_name, "Incomplete", task.get('title')])

    # Export data to CSV
        csv_file_name=f"{user_id}.csv"
        with open(csv_file_name, mode='w', newline='') as file:
            writer=csv.writer(file)
            writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(task_data
                    print(f"CSV file '{csv_file_name}' created successfully."))
