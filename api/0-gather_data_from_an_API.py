#!/usr/bin/python3
"""
Script that fetches and displays an employee's TODO list progress
from JSONPlaceholder API
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch employee data
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Error: Could not fetch employee data")
        sys.exit(1)
    
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    # Fetch todos for the employee
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print(f"Error: Could not fetch TODO data")
        sys.exit(1)
    
    todos = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]
    num_completed = len(completed_tasks)
    
    # Display results
    print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
    
    # Display completed task titles
    for task in completed_tasks:
        print(f"\t {task.get('title')}")