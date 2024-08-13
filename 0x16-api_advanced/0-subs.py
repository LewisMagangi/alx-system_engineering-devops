#!/usr/bin/python3
'''
A function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
'''
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditClient/0.1 (by Jazzlike-Plum-929)'}
    response = requests.get(url, headers=headers)
    print(response)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        return 0
