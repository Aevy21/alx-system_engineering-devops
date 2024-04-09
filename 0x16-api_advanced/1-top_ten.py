#!/usr/bin/python3
"""
This module contains a function that prints the titles of the
top 10 hottest posts for a specified subreddit
"""

import requests


def top_ten(subreddit):
    """
    prints the tites of the top 10 hottest posts for a specified subreddit

    subreddit: (string) - the subreddit to be queried
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json().get('data', {})
    children = data.get('children', [])
    
    if not children:
        print(None)
        return
    
    print("Top 10 hot posts in r/{}:".format(subreddit))
    for child in children[:10]:
        print(child.get('data', {}).get('title'))
