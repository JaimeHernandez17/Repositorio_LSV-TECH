from django.contrib.auth.models import User, Group
from rest_framework import serializers


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]
