#!/usr/bin/python3
"""Module to gather data from an API"""

import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_info = user_response.json()
    todos_info = todos_response.json()

    employee_name = user_info.get("name")
    
    completed_tasks = []
    for task in todos_info:
        if task.get("completed") is True:
            completed_tasks.append(task)
    
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_info)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_number_of_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))