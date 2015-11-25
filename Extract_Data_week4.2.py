import urllib
from BeautifulSoup import *

sample_data = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"
actual_data = " https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Jasmina.html"


def links(inp, pos, count):
    url = inp
    for i in range(count):
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        url = tags[pos].get('href', None)
        print "Retrieving: ", url

links(actual_data, 17, 7)
