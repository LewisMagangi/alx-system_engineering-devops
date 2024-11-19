#!/usr/bin/python3
"""
For an employee ID, returns information about their todo list progress.
"""
import csv
import json
import requests
import sys


def get_employee_to_do_progress(employee_id):
    """
    Fetch and display todo list progress for a given employee ID.
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    try:
        # Get single user directly using their ID
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        user = user_response.json()
        employee_name = user.get('name')

        # Get todos for the employee
        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todos_response.raise_for_status()
        todos = todos_response.json()

        # Calculate progress
        total = len(todos)
        completed_tasks = [task for task in todos if task.get('completed')]
        num = len(completed_tasks)

        # Display progress
        print(f"Employee {employee_name} is done with tasks({num}/{total}):")

        # Display completed task titles
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

        # Export to a csv file
        file_name = f'{employee_id}.csv'
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in todos:
                writer.writerow([employee_id, employee_name,
                                 task.get('completed'), task.get('title')])

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch data from API: {e}", file=sys.stderr)
        sys.exit(1)
    except (KeyError, ValueError) as e:
        print(f"Error: Invalid data received from API: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>", file=sys.stderr)
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_to_do_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.", file=sys.stderr)
        sys.exit(1)
