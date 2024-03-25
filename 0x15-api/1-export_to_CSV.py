#!/usr/bin/python3
"""This module fetches employer information from
`jsonplaceholder` API using requests module
and exports tasks data in CSV format

Modules used:
- json: Provides functions for working with JSON data.
- requests: Sends HTTP requests to the API and handles responses.
- sys.argv: Accesses command-line arguments to get the user ID from the command line.
- csv: Works with CSV files for writing task data to a CSV file.
"""

import json
import requests
from sys import argv
import csv

def export_tasks_to_csv(user_id, employee_name, tasks):
    task_data = []
    for task in tasks:
        if task.get("completed"):
            task_data.append([user_id, employee_name, "Completed", task.get('title')])
        else:
            task_data.append([user_id, employee_name, "Incomplete", task.get('title')])

    csv_file_name = f"{user_id}.csv"
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(task_data)

    print(f"CSV file '{csv_file_name}' created successfully.")

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

    # Export data to CSV using the function
    export_tasks_to_csv(user_id, employee_name, all_tasks)
