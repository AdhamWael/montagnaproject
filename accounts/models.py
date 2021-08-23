from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models.fields import CharField


# Create your models here.


class Product(models.Model):
    product_name = CharField(max_length=100)
    product_classes = CharField(max_length=100, default="")
    product_image1 = ImageField(upload_to = "productImages")
    product_image2 = ImageField(upload_to = "productImages")
    product_image3 = ImageField(upload_to = "productImages")