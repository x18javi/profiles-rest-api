from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Serializers a name field to test API view """
    name = serializers.CharField(max_length=10)
