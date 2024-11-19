#!/usr/bin/python3
"""
For an employee ID, returns information about the todo list progress.
"""
import requests
import sys


def get_employee_to_do_progress(employee_id):
    """
    Fetch and display todo list progress for a given employee ID.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    try:
        # Get employee information
        user_response = requests.get(f'{base_url}/users')
        user_response.raise_for_status()
        users = user_response.json()
        employee_name = None

        for user in users:
            if user.get('id') == employee_id:
                employee = user
                break
            
        if not employee:
            raise ValueError(f"No employee found with ID {employee_id}")

        employee_name = employee.get('name')


        # Get todos for the employee
        todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
        todos_response.raise_for_status()
        todos = todos_response.json()

        # Calculate progress
        t_tasks = len(todos)
        completed_tasks = [task for task in todos if task.get('completed')]
        no = len(completed_tasks)

        # Display progress
        print(f'Employee {employee_name} is done with tasks({no}/{t_tasks}):')
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
