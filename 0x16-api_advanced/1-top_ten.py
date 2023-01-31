#!/usr/bin/python3
"""
Function that queries reddit api and print titles of the
first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """ Queries reddit api. """
    api_header = {
            'User-Agent': 'Mozilla/5.0'
    }
    api_url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    api_res = requests.get(api_url, headers=api_header, allow_redirects=False)
    if api_res.status_code != 200:
        print(None)
    else:
        api_data = api_res.json().get('data')
        for children in api_data.get('children'):
            print(children.get('data').get('title'))
