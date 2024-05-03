# task_manager.py

import json


# Function to load tasks from a JSON file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


# Function to save tasks to a JSON file
def save_tasks(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


# Function to get tasks for a specific user
def get_user_tasks(user_name, tasks_data):
    return tasks_data.get(user_name, [])


# Function to update tasks for a specific user
def update_user_tasks(user_name, tasks, tasks_data):
    tasks_data[user_name] = tasks
    save_tasks('tasks.json', tasks_data)
