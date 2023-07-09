from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Generous(models.Model):
    cat_title = models.CharField(max_length=200)
    cat_description = models.TextField()

    def __str__(self):
        return self.cat_title

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    generous = models.ForeignKey(Generous,on_delete=models.CASCADE)
    isbn = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    discount_price = models.IntegerField()
    image = models.ImageField(upload_to="images/",null=True,blank=True)

    def __str__(self):
        return self.title