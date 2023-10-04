from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        data=request.data
        data['user']=request.user.id
        serializer=Blogserializer(data=data)
        if not serializer.is_valid():
            return Response({
                'data':serializer.errors,
                'msg':'something went wrong'
            })
        serializer.save()

        return Response({
                'data':serializer.data,
                'msg':'User created successfully'
            })



