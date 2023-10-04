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

    def get(self,request):
        blog=Blog.objects.filter(user=request.user)
        serializer=Blogserializer(blog,many=True)
        return Response({
                'data':serializer.data,
                'msg':'data created by you'
            })


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
    def patch(self,request):

        data=request.data
        blog=Blog.objects.filter(uid=data.get('uid'))

        if not blog.exists():
            return Response({
                'data':'',
                'msg':'Blog not found'
            })
        
        if request.user != blog[0].user:
            return Response({
                'data':'',
                'msg':'you are not authorized to changed'
            })
        
        serializer=Blogserializer(blog[0],data=data,partial=True)
        if not serializer.is_valid():
         

          return Response({
                'data':serializer.data,
                'msg':'Blog not updated successfully'
            })
        serializer.save()
        return Response({
                'data':serializer.data,
                'msg':'Blog updated successfully'
            })
    

    def delete(self,request):
        data=request.data
        blog=Blog.objects.filter(uid=data.get('uid'))

        if not blog.exists():
            return Response({
                'data':'',
                'msg':'Blog not found'
            })
        
        if request.user != blog[0].user:
            return Response({
                'data':'',
                'msg':'you are not authorized to changed'
            })
        
        blog[0].delete()
        return Response({
                'data':'',
                'msg':'data deleted successfully'
            })





