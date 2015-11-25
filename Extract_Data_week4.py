import urllib
from BeautifulSoup import *

sample_data = "http://python-data.dr-chuck.net/comments_42.html"
actual_data = "http://python-data.dr-chuck.net/comments_183052.html"

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()


soup = BeautifulSoup(html)

tags = soup('span')

count = []
for tag in tags:
    count.append(int(tag.contents[0]))

print "Sum: ", sum(count)