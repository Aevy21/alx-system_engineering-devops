#!/usr/bin/python3
"""
This module contains a function that returns the number of
subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers or 0 if subreddit is invalid.
    """
    headers = {'User-Agent': 'Aevy21 (by /u/Aevy21'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        # Extract number of subscribers from the response data
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    return 0
