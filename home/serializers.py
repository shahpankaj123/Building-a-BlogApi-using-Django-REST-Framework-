from rest_framework import serializers
from .models import Blog

class Blogserializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        exclude=['created_at','updated_at']