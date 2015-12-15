import urllib
import xml.etree.ElementTree as ET


test_url = "http://python-data.dr-chuck.net/comments_42.xml"
url = "http://python-data.dr-chuck.net/comments_183049.xml"

# url = raw_input("Enter URL: ")

xml = urllib.urlopen(url).read()

tree = ET.fromstring(xml)

counts = tree.findall('.//count')
total = 0
for count in counts:
    total += int(count.text)

print "Count: ", len(counts)
print "Sum: ", total

# makeing some iu changes



