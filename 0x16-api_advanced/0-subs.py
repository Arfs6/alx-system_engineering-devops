#!/usr/bin/python3
"""Using the reddit api."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers of a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'arfs6'}, allow_redirects=False)
    json = response.json()
    if response.status_code != 200 or json['kind'] != 't5':
        return 0
    return json['data']['subscribers']
