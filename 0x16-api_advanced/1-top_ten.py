#!/usr/bin/python3
'''
A function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'Custom'}
    response = requests.get(
        url,
        headers=headers,
        )
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for i in range(min(10, len(posts))):
            print(posts[i].get('data', {}).get('title', ''))
    else:
        print(None)
