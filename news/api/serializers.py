from rest_framework import serializers
from .models import News_data

# class Data_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = News_data
#         fields = '__all__'


class Data_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return News_data.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.type = validated_data.get("type", instance.type)
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance
