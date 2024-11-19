#!/usr/bin/python3
"""
For an employee ID, returns information about their TODO list progress.
"""
import json
import requests
import sys

'''
def get_employee_to_do_progress(employee_id):
    """
    Fetch and display TODO list progress for a given employee ID.
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
    response = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            sys.argv[1])
    dicti = json.loads(response.text)
    name = dicti.get('name')
    response = requests.get("https://jsonplaceholder.typicode.com/todos/" +
                            "?userId=" + sys.argv[1])
    todos = json.loads(response.text)
    tasks = len(todos)
    completed = [task for task in todos if task.get('completed')]
    done = len(completed)
    print("Employee {} is done with tasks({}/{}):".format(name, done, tasks))
    for task in completed:
        print("\t", task.get('title'))