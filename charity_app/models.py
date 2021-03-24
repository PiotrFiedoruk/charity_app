from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Institution(models.Model):
    ORGANISATION_TYPE = (
        (1, 'fundacja'),
        (2, 'organizajca pozarządowa'),
        (3, 'zbiórka lokalna'),
    )
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    type = models.IntegerField(choices=ORGANISATION_TYPE, default='fundacja')
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
