from rest_framework import serializers
from .models import News_data

# class Data_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = News_data
#         fields = ['title', 'type', 'content']

class Data_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=500)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return News_data.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.type = validated_data.get('type', instance.type)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

