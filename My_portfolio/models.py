from django.db import models
from django.contrib.auth.models import User

# Create your models here.
options=[["Commercial","Commercial"],["Personal","Personal"]]
class Work(models.Model):
    Category=models.CharField(max_length=100,null=True,choices=options)
    title=models.CharField(max_length=100,null=True)
    img1 = models.FileField(null=True)
    img2 = models.FileField(null=True)
    img3 = models.FileField(null=True)
    short_description=models.TextField(null=True)
    long_description=models.TextField(null=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title=models.CharField(max_length=100,null=True)
    img=models.FileField(max_length=100,null=True)
    short_description=models.TextField(null=True)
    long_description=models.TextField(null=True)

    def __str__(self):
        return self.title


