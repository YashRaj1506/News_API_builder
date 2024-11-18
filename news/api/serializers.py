from rest_framework import serializers
from news.api.models import News_data


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News_data
        fields = ['title','type','content']

