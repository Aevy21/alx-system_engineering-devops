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

    if subreddit is not None and type(subreddit) is str:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {"User-Agent": "api-practice (by /u/Aevy21)"}
        params = {"limit": 10}

        reddit_resp = requests.get(url, params=params, headers=headers,
                                   allow_redirects=False).json()

        reddit_response_data = reddit_resp.get("data", {})

        if reddit_response_data:
            for data_entry in reddit_response_data:
                if data_entry == "children":
                    for entry in reddit_response_data[data_entry]:
                        print(entry.get("data", {}).get("title", None))
                    return

    print(None)
