#!/usr/bin/python3
""" Get the 10 hot posts"""

import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit."""

    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    payload = {'limit': 10, 'sort': 'top'}
    headers = {'User-agent': 'your bot 0.1'}

    try:
        rests = requests.get(url, params=payload, headers=headers).json()
        topTen = rests["data"]["children"]
        for item in topTen:
            print(item["data"]["title"])

    except:
        print('None')
