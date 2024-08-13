#!/usr/bin/python3
'''
A function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
Return 0 if the subreddit is not valid
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
