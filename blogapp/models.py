from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    id = models.BigAutoField(primary_key=True,null=False)
    profile_picture=models.ImageField(null=True,blank=True,upload_to='static/images')
    fb_url=models.CharField(max_length=255,blank=True,null=True)
    website_url=models.CharField(max_length=255,blank=True,null=True)
    twitter_url=models.CharField(max_length=255,blank=True,null=True)
    insta_url=models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title= models.CharField(max_length=250)
    id = models.BigAutoField(primary_key=True,null=False)
    header_image=models.ImageField(blank=True, null=True,upload_to='static/images')
    author=models.ForeignKey(User,on_delete= models.CASCADE)
    body= RichTextField()
    post_date=models.DateField(auto_now_add=True)
    category= models.CharField(max_length=255, default='coding')
    likes=models.ManyToManyField(User,related_name='blog_posts')
    

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        #return reverse("article_detail", kwargs={"pk": self.pk})
        return reverse('home')
