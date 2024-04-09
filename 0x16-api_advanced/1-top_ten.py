#!/usr/bin/python3

"""
This module provides a function to print the titles of the first 10 hot posts listed for a given subreddit using the Reddit API.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Construct the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Define custom User-Agent header
    headers = {'User-Agent': 'RedditTopPosts/2.0'}

    # Make a GET request to the Reddit API, disallowing redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract the list of posts
        posts = data.get('data', {}).get('children', [])

        # Print the titles of the first 10 posts
        for i, post in enumerate(posts[:10], start=1):
            print(f"{i}. {post.get('data', {}).get('title', 'Title not found')}")
    else:
        # If the response status code is not 200, print None
        print("None")
