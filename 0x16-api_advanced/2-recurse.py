#!/usr/bin/python3
"""
Recursive function that queires reddit api and return list containing
titles of hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recursive function to query reddit api. """
    api_header = {'User-Agent': 'Mozilla/5.0'}
    api_params = {'after': after}
    api_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    api_res = requests.get(
                            api_url,
                            headers=api_header,
                            params=api_params,
                            allow_redirects=False
                          )
    if api_res.status_code != 200:
        return(None)

    api_data = api_res.json().get('data')
    after = api_data.get('after')
    hot_list += list(map(
                          lambda children: children.get('data').get('title'),
                          api_data.get('children')
                       ))
    if after is None:
        return(hot_list)
    return recurse(subreddit, hot_list, after)
