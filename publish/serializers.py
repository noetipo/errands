from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from publish.models import Author


class AuthorSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Author
        fields = '__all__'
