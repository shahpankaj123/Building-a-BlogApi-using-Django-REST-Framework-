from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Basemodel(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract=True

class Blog(Basemodel):
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='Blog')
    blog_title=models.CharField(max_length=100)
    blog_desc=models.TextField()      


    def __str__(self) -> str:
        return self.blog_title

