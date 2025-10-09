from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField()
    email = models.CharField()
    mobile = models.PositiveIntegerField(max_length=10)
    address = models.TextField()
    password = models.CharField()

    def __str__(self):
        return self.name


class Farmer(models.Model):
    fid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.PositiveIntegerField(max_length=10)
    address = models.TextField()
    village = models.CharField(max_length=100)
    aadharno = models.CharField(max_length=12)
    password = models.CharField(max_length=100)  

    def __str__(self):
        return self.name
    

class AllProducts(models.Model):
    fid = models.PositiveIntegerField(default=0)
    farmer_name = models.CharField(max_length=100)
    farmer_location = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=300)
    cultivated_date = models.DateTimeField()
    experiry_date = models.DateTimeField()
    photo = models.ImageField(upload_to='product/', default='product/default.jpg')


    def __str__(self):
        return self.product_name


