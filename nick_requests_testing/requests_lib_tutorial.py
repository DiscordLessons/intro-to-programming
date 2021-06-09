# https://realpython.com/python-requests/

import requests

def github_requests():
    response = requests.get('https://api.github.com')
    print(response)
    print(response.json())

github_requests()