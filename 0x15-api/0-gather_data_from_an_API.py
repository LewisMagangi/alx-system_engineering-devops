#!/usr/bin/python3
"""
For an employee ID, returns information about their todo list progress.
"""
import json
import requests
import sys

'''
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
'''

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Get the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filter completed tasks and count them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks one by one with indentation
    [print("\t {}".format(complete)) for complete in completed]
