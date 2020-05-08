#!/usr/bin/python3
""" Get the numbers of subscribers """

import requests


def number_of_subscribers(subreddit):
    """Function that queries the Reddit API
    and returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    payload = {'limit': 1}
    headers = {'User-agent': 'your bot 0.1'}

    try:
        rests = requests.get(url, params=payload, headers=headers).json()
        return (rests["data"]["children"][0]["data"]["subreddit_subscribers"])

    except:
        return (0)
