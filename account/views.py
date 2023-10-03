from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *


class RegisterView(APIView):

    def post(self,request):
        data=request.data
        serializer=Registerserializer(data=data)

        if not serializer.is_valid():
            return Response({
                'data':serializer.errors,
                'msg':'something went wrong'
            })
        serializer.save()
        return Response({
                'data':'',
                'msg':'User created successfully'
            })



# Create your views here.
