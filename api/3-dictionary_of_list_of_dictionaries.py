#!/usr/bin/python3
import requests
import json

def main():
    # API URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users
    users_response = requests.get(users_url)
    users_response.raise_for_status()
    users = users_response.json()
    
    # Create a mapping: user_id (int) -> username
    user_dict = {user["id"]: user["username"] for user in users}

    # Fetch all TODOs
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos = todos_response.json()

    # Prepare the JSON structure
    all_data = {}
    for task in todos:
        user_id = task["userId"]  # keep as integer
        if user_id not in all_data:
            all_data[user_id] = []
        all_data[user_id].append({
            "username": user_dict[user_id],  # integer key works now
            "task": task["title"],
            "completed": task["completed"]
        })

    # Convert keys to strings before writing JSON (optional, matches example)
    all_data_str_keys = {str(k): v for k, v in all_data.items()}

    # Write to JSON file
    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(all_data_str_keys, f, indent=4)

if __name__ == "__main__":
    main()
