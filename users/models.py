from django.db import models

# Create your models here.
class ImHanceUser(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=250)
    logged = models.BooleanField(default=False)
class Pictures(models.Model):
    user_id = models.ForeignKey(ImHanceUser,on_delete=models.CASCADE)
    base64_image = models.TextField()