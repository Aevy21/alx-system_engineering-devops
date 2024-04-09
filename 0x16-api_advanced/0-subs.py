#!/usr/bin/python3

"""
This module provides a function to retrieve the number of subscribers for a given subreddit using the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
        """
            Retrieve the number of subscribers for a given subreddit.

                Args:
                        subreddit (str): The name of the subreddit.

                            Returns:
                                    int: The number of subscribers of the subreddit. Returns 0 if the subreddit is invalid.
                                        """
                                            # Construct the URL for the
                                            # subreddit
                                                url = f"https://www.reddit.com/r/{subreddit}/about.json"

                                                        # Define custom
                                                        # User-Agent header
                                                            headers = {
                                                                'User-Agent': 'CustomUserAgent'}

                                                                    # Make a
                                                                    # GET
                                                                    # request
                                                                    # to the
                                                                    # Reddit
                                                                    # API
                                                                        response = requests.get(
                                                                            url, headers=headers)

                                                                                # Check
                                                                                # if
                                                                                # the
                                                                                # response
                                                                                # is
                                                                                # successful
                                                                                # (status
                                                                                # code
                                                                                # 200)
                                                                                    if response.status_code == 200:
                                                                                                # Parse
                                                                                                # JSON
                                                                                                # response
                                                                                                        data = response.json()

                                                                                                                        # Extract
                                                                                                                        # the
                                                                                                                        # number
                                                                                                                        # of
                                                                                                                        # subscribers
                                                                                                                        # from
                                                                                                                        # the
                                                                                                                        # response
                                                                                                                        # data
                                                                                                                                subscribers = data[
                                                                                                                                    'data']['subscribers']

                                                                                                                                                # Return
                                                                                                                                                # the
                                                                                                                                                # number
                                                                                                                                                # of
                                                                                                                                                # subscribers
                                                                                                                                                        return subscribers
                                                                                                                                                        else:
                                                                                                                                                                    # If
                                                                                                                                                                    # the
                                                                                                                                                                    # response
                                                                                                                                                                    # status
                                                                                                                                                                    # code
                                                                                                                                                                    # is
                                                                                                                                                                    # not
                                                                                                                                                                    # 200,
                                                                                                                                                                    # return
                                                                                                                                                                    # 0
                                                                                                                                                                            return 0

                                                                                                                                                                        # Example
                                                                                                                                                                        # usage:
                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                subreddit = 'python'
                                                                                                                                                                                    print(number_of_subscribers(subreddit))

