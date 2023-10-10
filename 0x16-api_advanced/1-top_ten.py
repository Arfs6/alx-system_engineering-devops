#!/usr/bin/python3
"""Using reddit api."""
import requests


def top_ten(subreddit):
    """Print the title of the top ten hot reddit posts in a sub redit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'arfs6'}, allow_redirects=False)
    if response.status_code != 200:
        return
    json = response.json()
    data = json['data']['children']
    for post in data:
        print(post['data']['title'])
