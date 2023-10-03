from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class Registerserializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('username already exists')
        
        return data
    
    def create(self, validated_data):
        user=User.objects.create(username=validated_data['username'])
        print(validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        
        return validated_data
    
class Loginserializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):
        if not User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('username doesnot exists')
        
        return data
    
    def get_jwt_token(self,data):

        user=authenticate(username=data['username'],password=data['password'])

        if not user:
            return {'msg':'sorry username or password not matched'}
        
        refresh = RefreshToken.for_user(user)

        return {
        'msg':'login successfully',
        'data':{'token': {'refresh': str(refresh),
        'access': str(refresh.access_token)},}
        }

        







