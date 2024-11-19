#!/usr/bin/python3
"""Export all employees' todo lists to a JSON file."""
import json
import requests
import sys


def export_all_employees_todos():
    """
    Export todo list information for all employees to a JSON file.

    Returns:
        dict: Dictionary containing todo list information for all employees
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    try:
        # Get all users
        users_response = requests.get(f"{base_url}/users")
        users_response.raise_for_status()
        users = users_response.json()

        # Create a dictionary containing to-do list of all employees
        data_to_export = {}
        for user in users:
            user_id = user["id"]
            todos_response = requests.get(f"{base_url}/todos?userId={user_id}")
            todos_response.raise_for_status()
            todo_list = todos_response.json()

            data_to_export[user_id] = [
                {
                    "username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                }
                for todo in todo_list
            ]

        # Write data to JSON file
        with open('todo_all_employees.json', 'w') as jsonfile:
            json.dump(data_to_export, jsonfile, indent=2)

        print("Todo list exported successfully to todo_all_employees.json")
        return data_to_export

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch data from API: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    export_all_employees_todos()
