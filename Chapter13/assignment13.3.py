import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

address = raw_input('Enter location: ')
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url

data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'
js = json.loads(str(data))

print 'Place id', js["results"][0]["place_id"]

