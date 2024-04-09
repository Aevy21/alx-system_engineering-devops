#!/usr/bin/python3

"""
This module provides a function to retrieve the total number of subscribers for a given subreddit using the Reddit API.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The total number of subscribers if the subreddit is valid, otherwise 0.
    """
    # Construct the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Define custom User-Agent header
    headers = {'User-Agent': 'RedditSubscribers'}

    # Make a GET request to the Reddit API, disallowing redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract the total number of subscribers (active + non-active)
        total_subscribers = data['data']['subscribers']

        # Return the total number of subscribers
        return total_subscribers
    else:
        # If the response status code is not 200, return 0
        return 0

if __name__ == "__main__":
    subreddit = "programming"
    print(number_of_subscribers(subreddit))
