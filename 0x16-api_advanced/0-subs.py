#!/usr/bin/python3
"""
This module contains a function that returns the number of
subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for  given subreddit.

    subreddit: (string) - the subreddit to be queried

    Return: 0 if the given subreddit is invalid; else the number
    of subscribers is returned
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "querying_reddit_subscribers"}

    reddit_response = requests.get(url, headers=headers,
                                   allow_redirects=False).json()

    subscribers = reddit_response.get("data", {}).get("subscribers", 0)
    return subscribers
