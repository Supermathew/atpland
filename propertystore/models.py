from django.db import models
from category.models import Category
from django.contrib.auth.models import User
from django.conf import settings


from django.urls import reverse
from accounts.models import Account
from embed_video.fields import EmbedVideoField


# Create your models here.

class Product(models.Model):
    property_name    = models.CharField(max_length=200, unique=True)
    owner_type = models.CharField(max_length=200)
    slug            = models.SlugField(max_length=200, unique=True,blank=True)
    description     = models.TextField(max_length=800, blank=True)
    property_cent    = models.IntegerField()
    property_squarefeet    = models.IntegerField()
    property_Water_Availability = models.CharField(max_length=200)
    property_transpaortation = models.CharField(max_length=200)
    price = models.IntegerField()
    tocken_amount   =models.IntegerField()
    images1          = models.ImageField(upload_to='photos/propertyphoto',)
    images2          = models.ImageField(upload_to='photos/propertyphoto',blank=True)
    images3          = models.ImageField(upload_to='photos/propertyphoto',blank=True)
    images4          = models.ImageField(upload_to='photos/propertyphoto',blank=True)
    video            =models.FileField(upload_to="video/%y",blank=True)
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    propertyowner   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video_url       = EmbedVideoField(blank=True,null=True,default="https://www.youtube.com/watch?v=DL77F7AWIl8")
    property_address = models.TextField(max_length=800, blank=True)
    property_pincode = models.IntegerField() 
    phonenumber      = models.IntegerField()
    urltest = models.TextField(blank=True)
    district         = models.CharField(max_length=200)
    propertylocation_url       = models.URLField(blank=True,null=True)
    verifyed    = models.BooleanField(default=False)




    def get_url(self):
        return reverse('property_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.property_name

    



  
