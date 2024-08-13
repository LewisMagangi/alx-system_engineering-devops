#!/usr/bin/python3
'''
A recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should return None.
'''

import requests

def top_ten(subreddit):
    url =  f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditClient/0.1 (by Jazzlike-Plum-929)'}
    response = requests.get(url, headers=headers)
    print(response)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        return None
