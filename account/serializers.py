from django.contrib.auth.models import User
from rest_framework import serializers



class Registerserializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('username already exists')
        
        return data
    
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        return validated_data
    



