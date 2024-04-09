#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    # Construct the URL for the Reddit API
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set custom user agent header as required by Reddit API
    headers = {
        "User-Agent": "Aevy21"
    }

    # Parameters for the Reddit API request
    params = {
        "after": after,
        "limit": 100
    }

    # Make the HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False
                            )

    # Check if the subreddit is valid (status code 404 indicates not found)
    if response.status_code == 404:
        return None
    else:
        # Extract JSON response data
        results = response.json().get("data")
        after = results.get("after")

        # Extract titles from the response and append them to the hot_list
        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))

        # If there are more pages of results,
        # recursively call the function with updated parameters
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            # Return the final list of hot post titles
            return hot_list
