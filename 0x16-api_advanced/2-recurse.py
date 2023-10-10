#!/usr/bin/python3
"""Using reddit api."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot posts in a sub reddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {}
    if after:
        params['after'] = after
    response = requests.get(url, headers={'User-Agent': 'arfs6'}, allow_redirects=False, params=params)
    if response.status_code != 200:
        return
    json = response.json()
    hot_list.extend([data['data']['title'] for data in json['data']['children']])
    if json['data']['after']:
        recurse(subreddit, hot_list=hot_list, after=json['data']['after'])
    return hot_list
