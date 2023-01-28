from django.db import models
from typing import Iterable
from django.contrib.postgres.fields import ArrayField



# Create your models here.

class Contents(models.Model): #Content per User
    id_user = models.IntegerField()
    number_content = models.IntegerField()
    text_content = models.TextField(max_length=300)
    post_date = models.DateTimeField()
    like_count = models.IntegerField()
    coments = ArrayField(models.TextField(null=True))
    image = models.ImageField(default="", upload_to='images/')

class Content_tag(models.Model): #Tag per content u/ Search Engine
    tag_content = models.CharField(max_length=25)
    tag_click = models.IntegerField()
    tag_used = models.IntegerField()


class User_additions(models.Model):
    id_user = models.IntegerField(default=0)
    followed = ArrayField(ArrayField(models.TextField()))
    follower = ArrayField(ArrayField(models.TextField()))
    content_count = models.IntegerField(default=0)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    id_user = models.IntegerField()



class Content(models.Model):
    id_user = models.IntegerField(default=0)
    number_content = models.IntegerField(default=0)
    text_content = models.TextField(max_length=300, null=True)
    post_date = models.DateTimeField(null=True)
    like_count = models.IntegerField(default=0)
    coments = []


class Coments(models.Model): #Menampilkan komentar untuk content tertentu
    comment_text = models.TextField(max_length=150)
    id_commenter = models.IntegerField()
    id_contentCreator = models.IntegerField()
    number_content = models.IntegerField()