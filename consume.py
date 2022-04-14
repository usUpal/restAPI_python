import json

import requests

response = requests.get('https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow')

for data in response.json()['items']:
    # print(data['owner'])
    # print(data['tags'])
    if data["answer_count"] < 1:
        print(data['title'])
        print(data['link'])
    print()
