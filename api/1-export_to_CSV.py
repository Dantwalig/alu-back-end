#!/usr/bin/python3
import requests
import sys
import csv

def main():
    # Check if employee ID is given
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py EMPLOYEE_ID")
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
    employee_name = user_data.get("username")

    # Get TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error fetching TODO list for employee {employee_id}")
        sys.exit(1)
    todos = todos_response.json()

    # CSV filename
    filename = f"{employee_id}.csv"

    # Write CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

if __name__ == "__main__":
    main()
