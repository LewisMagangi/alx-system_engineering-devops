#!/usr/bin/python3
'''
a recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
Hint: The Reddit API uses pagination for separating pages of responses.
'''
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    If not a valid subreddit, return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'Custom'}
    response = requests.get(
        url,
        headers=headers,
        params={"after": after},
        )
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for i in range(min(10, len(posts))):
            print(posts[i].get('data', {}).get('title', ''))
            hot_list.append(title)
        after = req.json().get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
