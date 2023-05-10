import requests
import json
from pprint import pprint


url = 'https://randomuser.me/api?results=30&gender=male'

lst = []
res = requests.get(url=url)

txtData = res.text

users = json.loads(txtData)

for user in users['results']:
    lst.append(user['name']['first'] + ' ' + user['name']['last'])

print(len(lst))

