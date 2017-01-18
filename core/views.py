from django.shortcuts import render
from rest_framework import viewsets
from core.serializers import SearchSerializer
from core.models import Search


def home(request):
    data = {}
    return render(request, 'core/home.html', data)


class SearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Searchs to be viewed or edited.
    """
    queryset = Search.objects.all().order_by('-date')[:1]
    serializer_class = SearchSerializer
