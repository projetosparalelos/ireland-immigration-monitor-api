from core.models import Search
from rest_framework import serializers


class SearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Search
        fields = ('result', 'date')
