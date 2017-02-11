from django.shortcuts import HttpResponse
import ssl
import json
from ireland_gnib.settings import OPENWEATHERAPI

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


def search(url):
    req = urllib2.Request(url, headers={ 'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' })
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    info = urllib2.urlopen(req, context=gcontext).read()
    info = json.loads(info.decode('utf-8'))
    return info


def weather(request, city_code):
    url = 'http://openweathermap.org/data/2.5/weather?id={city_id}&appid' \
          '={api}?units=metric'.format(city_id=city_code, api=OPENWEATHERAPI)
    url = 'http://samples.openweathermap.org/data/2.5/find?q=London&units=metric&appid=b1b15e88fa797225412429c1c50c122a1'
    result = search(url)
    return HttpResponse(json.dumps(result), content_type="application/json")
