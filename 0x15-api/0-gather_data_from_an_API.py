#!/usr/bin/python3
"""Get data from the json
place holder api."""


import requests
import sys


def run():
    """Begin code execution"""
    url = 'https://jsonplaceholder.typicode.com/'
    name = requests.get(
        url + f"users/{sys.argv[1]}"
    ).json().get('name')
    if not name:
        return  # user doesn't exists
    response = requests.get(url + f"users/{sys.argv[1]}/todos")
    json = response.json()
    doneTasks = [task for task in json if task.get('completed') is True]
    print(
        f"Employee {name} is done with",
        f"tasks({len(doneTasks)}/{len(json)}):"
    )
    for task in doneTasks:
        print(f"\t{task.get('title')}")


if __name__ == '__main__':
    run()
