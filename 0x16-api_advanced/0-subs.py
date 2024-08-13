#!/usr/bin/python3
'''
A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
'''
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    # url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # headers = {'User-Agent': 'Custom'}
    response = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Mozilla/5.0"},
        )
    if response.status_code == 200:
        # data = response.json()
        return response.json().get("data", {}).get("subscribers", 0)
        # print(data)
    else:
        return 0
