#!/usr/bin/python3
"""
    a Python script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        request the user's info by employee ID
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        json to dictionary
    """
    employee = json.loads(request_employee.text)
    """
        get employee name
    """
    employee_name = employee.get("name")

    """
        Make a request to the API to get the employee's TODO list
    """
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        dictionary to store task status
    """
    tasks = {}
    """
        convert json to list of dictionaries
    """
    employee_todos = json.loads(request_todos.text)
    """
        loop through dictionary & get completed tasks
    """
    for dictionary in employee_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        return name, total number of tasks & completed tasks
    """
    EMPLOYEE_NAME = employee_name: ok
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for k, v in tasks.items():
        if v is True:
            print("\t {}".format(k))
