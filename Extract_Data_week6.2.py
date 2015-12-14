import urllib
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

address = raw_input("Enter address:")

url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address})

data = urllib.urlopen(url).read()

js = json.loads((data))

id = js["results"][0]["place_id"]
print "Place id: ", id




