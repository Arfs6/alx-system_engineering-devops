#!/usr/bin/python3
"""Get data from the json
place holder api."""


import json
import requests


def getTasks(id, username):
    """Returns all the tasks of the user with id @id."""
    url = 'https://jsonplaceholder.typicode.com/'
    response = requests.get(url + f"users/{id}/todos")
    tasks = response.json()
    formattedTasks = [
        {
            'username': username,
            'task': task.get('title'),
            'completed': task.get('completed'),
        }
        for task in tasks
    ]
    return formattedTasks


def run():
    """Begin code execution"""
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users').json()
    usersTasks = {}
    for user in users:
        usersTasks[user.get('id')] = getTasks(user.get('id'), user.get('name'))
    with open('todo_all_employees.json', 'w') as jsonFile:
        json.dump(usersTasks, jsonFile)


if __name__ == '__main__':
    run()
