from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    text = models.CharField(max_length=300,default='')
    created_at=models.DateTimeField(null=True,blank=True)
    updated_at = models.DateTimeField(null=True,blank=True)


