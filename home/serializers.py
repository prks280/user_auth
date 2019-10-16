from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Neta, Rating


class NetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neta
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    # neta = serializers.StringRelatedField()

    class Meta:
        model = Rating
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
