from django.db import models
from django.contrib.auth.models import User


class student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    def __str__(self):
        return self.first_name+' '+self.last_name
