#!/usr/bin/python3
"""
This module contains a function that returns the number of
subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    subreddit: (string) - the subreddit to be queried

    Return: 0 if the given subreddit is invalid; else the number
    of subscribers is returned
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyRedditScraper/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        reddit_response = response.json()
        subscribers = reddit_response.get("data", {}).get("subscribers", 0)
        return subscribers
    else:
        return 0
