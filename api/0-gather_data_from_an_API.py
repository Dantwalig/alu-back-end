#!/usr/bin/env python3
import requests
import sys

def main():
    # Check if employee ID is given
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer")
        sys.exit(1)

    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Get employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error fetching employee with ID {employee_id}")
        sys.exit(1)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error fetching TODO list for employee {employee_id}")
        sys.exit(1)
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task["completed"]]
    number_done = len(done_tasks)

    # Print output
    print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    main()
