from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Pictures(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    base_64_picture = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
