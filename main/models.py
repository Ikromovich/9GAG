from django.db import models
from gag.helpers import UploadTo
from gag.mixins import TranslateMixin
from client.models import *
# Create your models here.
class Category(TranslateMixin,models.Model):
    translate_fields = ['name']
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)
    image = models.ImageField(upload_to=UploadTo("category"))

class Post(TranslateMixin,models.Model):
    translate_fields = ['name']
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True,on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="Izoh")
    file = models.FileField(verbose_name="Rasm/Video", upload_to=UploadTo("post"))
    like = models.IntegerField(default=0)
    dislike =models.IntegerField(default=0)
    added_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post_comment(TranslateMixin,models.Model):
    translate_fields=['name']
    parent = models.CharField(null=True,default=None)
    post = models.ForeignKey(Post, null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    comment= models.TextField(verbose_name="Izoh")
    image = models.ImageField(upload_to=UploadTo("comment"))
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)