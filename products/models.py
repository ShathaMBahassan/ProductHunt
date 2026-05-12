from django.db import models
from Users.models import Create_User 

class Product(models.Model):
    tilte = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to="images/")
    icon = models.ImageField(upload_to="images/")
    body = models.TextField()
    hunter = models.ForeignKey(Create_User, on_delete=models.CASCADE)

    def __str__(self):
        return f" the product is {self.tilte}"