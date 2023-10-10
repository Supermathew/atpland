from django.db import models
from django.conf import settings
from propertystore.models import Product
# Create your models here.


class Messagemodel(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='buyer')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='seller')
    property = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='property')
    messagebybuyer = models.TextField()
    buyerphonenumber = models.IntegerField(blank=True)
    def __str__(self):
        return self.buyer.first_name
