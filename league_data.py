import urllib
import json

# handler = urllib.urlopen('http://www.rsssf.com/tablesw/wal1928.html')
#
# for line in handler:
#     print line

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

#while True:
    #address = raw_input('Enter: ')

    #url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': address})

url = "http://www.football-data.org/v1/soccerseasons/351/teams"

print "Retriveing: ", url

uh = urllib.urlopen(url)
data = uh.read()

print data

js = json.loads(str(data))

name = js["teams"]

print "teams: ", name

    #print json.dumps(js, indent=4)

    #address = js["results"] [0] ["formatted_address"]

   # print address

