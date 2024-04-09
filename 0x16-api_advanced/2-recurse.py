#!/usr/bin/python3

"""recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit."""


import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])
    for child in children:
        hot_list.append(child['data']['title'])

    after = data.get('after')
    if after:
        recurse(subreddit, hot_list, after)
    else:
        return hot_list
