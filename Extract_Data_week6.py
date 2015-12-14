import urllib
import json

test_url = "http://python-data.dr-chuck.net/comments_42.json"
url = "http://python-data.dr-chuck.net/comments_183053.json"

url = raw_input("Enter URL: ")

info = urllib.urlopen(url).read()

data = json.loads(info)

total = 0

for item in data['comments']:
    total += int(item['count'])

print total
