from django.shortcuts import render
from rest_framework import viewsets
from tourism.serializers import PlaceSerializer
from .models import Place
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


def home(request):
    data = {}
    return render(request, 'core/home.html', data)


class PlacesViewSet(viewsets.ViewSet):
    """
    API endpoint that allows Places to be viewed or edited.
    """

    def list(self, request):
        queryset = Place.objects.all()
        serializer = PlaceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Place.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PlaceSerializer(user)
        return Response(serializer.data)
