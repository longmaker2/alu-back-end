#!/usr/bin/python3
"""gathers data from an API """

import json
import requests


def get_employee_task(employee_id):
    """Doc"""
    url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)

    user_info = requests.request('GET', url).json()

    employee_username = user_info["username"]
    todo = "https://jsonplaceholder.typicode.com/users/{}/todos"
    todo = todo.format(employee_id)
    todos_info = requests.request('GET', todo).json()
    return [
        dict(zip(["task", "completed", "username"],
                 [task["title"], task["completed"], employee_username]))
        for task in todos_info]


def get_employee_ids():
    """Doc"""
    user = "https://jsonplaceholder.typicode.com/users/"

    users_info = requests.request('GET', user).json()
    ids = list(map(lambda user: user["id"], users_info))
    return ids


if __name__ == '__main__':

    employee_id = get_employee_ids()

    with open('todo_all_employees.json', "w") as f:
        all_users = {}
        for employee_id in employee_id:
            all_users[str(employee_id)] = get_employee_task(employee_id)
        f.write(json.dumps(all_users))
