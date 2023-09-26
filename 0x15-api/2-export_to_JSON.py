#!/usr/bin/python3
"""Get data from the json
place holder api."""


import json
import requests
import sys


def run():
    """Begin code execution"""
    url = 'https://jsonplaceholder.typicode.com/'
    username = requests.get(url + f"users/{sys.argv[1]}").json().get('username')
    if not username:
        return  # user doesn't exists
    response = requests.get(url + f"users/{sys.argv[1]}/todos")
    tasks = response.json()
    formattedTasks = [
        {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        }
        for task in tasks
    ]
    userTasks = {sys.argv[1]: formattedTasks}
    with open(sys.argv[1] + '.json', 'w') as jsonFile:
        json.dump(userTasks, jsonFile)


if __name__ == '__main__':
    run()
