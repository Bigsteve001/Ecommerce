from distutils.command.upload import upload
from statistics import mode
from django.db import models
import profile

class home(models.Model):
    shoename=models.CharField(max_length=200,)
    picture=models.ImageField(upload_to='picture/',null=True)
    price=models.IntegerField(blank=True, null=True)
    description=models.CharField(max_length=200, blank=True)
    def __str__(self):
      return str(self.id)

class shoe(models.Model):
    newshoes_name=models.CharField(max_length=50, blank=True)
    newshoes_price=models.IntegerField(blank=True,null=True)
    newshoes_picture=models.ImageField(upload_to='new/',null=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) :
        return str(self.id)


class trending(models.Model):
    Trending_name=models.CharField(max_length=100, blank=True)
    Trending_price=models.IntegerField(blank=True, null=True)
    Trending_picture=models.ImageField(upload_to='trending/', null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
      return str(self.id)