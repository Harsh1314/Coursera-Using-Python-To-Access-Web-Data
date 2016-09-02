import urllib
import json


url = raw_input('Enter location: ')
print 'Retrieving', url

data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'

info = json.loads(data)
print 'Count:', len(info['comments'])

sum = 0

for item in info['comments']:
    sum += int(item['count'])

print 'Sum:',sum
