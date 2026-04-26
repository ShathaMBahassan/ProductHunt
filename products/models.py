from django.db import models

# Create your models here
class Create_User(models.Model):
    username = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)

    def __str__(self):
        return f"the user is {self.full_name}"
