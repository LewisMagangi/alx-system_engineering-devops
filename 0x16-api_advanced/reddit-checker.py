import requests

def check_subreddit_exists(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'RedditChecker/1.0.0 (by u/Jazzlike-Plum-929)'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return True  # Subreddit exists
    elif response.status_code == 404:
        return False  # Subreddit does not exist
    else:
        print(f"Error: Received status code {response.status_code}")
        return None  # Could be due to other issues like rate limiting or forbidden access

subreddit_name = 'nairobi'  # Replace with the subreddit you want to check
exists = check_subreddit_exists(subreddit_name)

if exists:
    print(f"The subreddit r/{subreddit_name} exists.")
elif exists == False:
    print(f"The subreddit r/{subreddit_name} does not exist.")
else:
    print("Could not determine if the subreddit exists due to an error.")

