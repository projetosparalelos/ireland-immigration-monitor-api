from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from core.serializers import SearchSerializer
from core.models import Search
import ssl
import json

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


def home(request):
    data = {}
    return render(request, 'core/home.html', data)


class SearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Searchs to be viewed or edited.
    """
    queryset = Search.objects.all().order_by('-date')[:1]
    serializer_class = SearchSerializer


urlRenewal = 'https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/(getApps4DTAvailability)?openpage&&cat=Study&sbcat=All&typ=Renewal&_=1479407403955';
urlNewGNIB = 'https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/(getAppsNear)?openpage&cat=Study&sbcat=All&typ=New&_=1483649646705';
urlWorkPermit = 'https://burghquayregistrationoffice.inis.gov.ie/Website/AMSREG/AMSRegWeb.nsf/(getAppsNear)?openpage&cat=Work&sbcat=All&typ=New&_=1484748845173';


def search(url):
    req = urllib2.Request(url, headers={ 'X-Mashape-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' })
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    info = urllib2.urlopen(req, context=gcontext).read()
    info = json.loads(info.decode('utf-8'))
    return info


def renewal(request):
    cons = search(urlRenewal)
    return HttpResponse(json.dumps(cons), content_type="application/json")


def new_GNIB(request):
    cons = search(urlNewGNIB)
    return HttpResponse(json.dumps(cons), content_type="application/json")


def work_permit(request):
    cons = search(urlWorkPermit)
    return HttpResponse(json.dumps(cons), content_type="application/json")
