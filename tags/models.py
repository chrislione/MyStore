from tkinter import CASCADE
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

class Tag(models.Model):
    label=models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
# we need a way of identifying and object to tag which might be in a different folder
    # 1. Type (product,video,article)
    # 2. ID   
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey()
    #content_type represent the type of model in our application
    # if you want to get the actualy object the tag is applied to 
class LikeItem(models.Model):
        user=models.ForeignKey(User, on_delete=models.CASCADE)
        content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
        content_object=GenericForeignKey()
        object_id=models.PositiveIntegerField()