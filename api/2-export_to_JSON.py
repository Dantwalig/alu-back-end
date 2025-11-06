#!/usr/bin/python3
import requests
import sys
import json

def main():
    # Check if employee ID is given
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py EMPLOYEE_ID")
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
    username = user_data.get("username")

    # Get TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error fetching TODO list for employee {employee_id}")
        sys.exit(1)
    todos = todos_response.json()

    # Prepare JSON structure
    json_data = {str(employee_id): []}
    for task in todos:
        json_data[str(employee_id)].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })

    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

if __name__ == "__main__":
    main()
