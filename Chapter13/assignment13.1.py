import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)

results = tree.findall('.//count')
print 'Count:',len(results)

sum = 0

for item in results:
    sum += int(item.text)

print 'Sum:', sum