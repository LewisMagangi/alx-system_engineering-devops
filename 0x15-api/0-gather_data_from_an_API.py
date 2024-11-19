#!/usr/bin/python3
"""
For an employee ID, returns information about their TODO list progress.
Uses JSONPlaceholder API to fetch employee and TODO data.
"""
import requests
import sys


def get_employee_to_do_progress(employee_id):
    """
    Fetch and display TODO list progress for a given employee ID.
    Args:
        employee_id: Integer ID of the employee
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    try:
        # Get all users
        users_response = requests.get(f'{base_url}/users')
        users_response.raise_for_status()
        users = users_response.json()

        # Find the specific employee
        employee = None
        for user in users:
            if user.get('id') == employee_id:
                employee = user
                break

        if not employee:
            raise ValueError(f"No employee found with ID {employee_id}")

        # Get todos for the employee
        todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
        todos_response.raise_for_status()
        todos = todos_response.json()

        # Calculate progress
        total_tasks = len(todos)
        completed_tasks = [task for task in todos if task.get('completed')]
        num_completed = len(completed_tasks)

        # Display progress
        print(f'Employee {employee.get("name")} is done with tasks'
              f'({num_completed}/{total_tasks}):')

        # Display completed task titles
        for task in completed_tasks:
            print(f'\t {task.get("title")}')

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
