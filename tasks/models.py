from django.db import models
from django.contrib.auth.models import User




class Users(models.Model):
    # user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    surname = models.CharField(max_length=30, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)







class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    user = models.ForeignKey(Users,default=False,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title