#!/usr/bin/python3
"""Get data from the json
place holder api."""


import csv
import requests
import sys


def run():
    """Begin code execution"""
    url = 'https://jsonplaceholder.typicode.com/'
    username = requests.get(url + f"users/{sys.argv[1]}").json().get('username')
    if not username:
        return  # user doesn't exists
    response = requests.get(url + f"users/{sys.argv[1]}/todos")
    json = response.json()
    rows = [[sys.argv[1], username, task.get('completed'), task.get('title')]
            for task in json]
    with open(sys.argv[1] + '.csv', 'w') as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        csvWriter.writerows(rows)


if __name__ == '__main__':
    run()
