from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(verbose_name="owner", to=User, on_delete=models.PROTECT)
    name = models.CharField(verbose_name="name", max_length=50)
    price = models.DecimalField(verbose_name="price", max_digits=12, decimal_places=2)
    image = models.ImageField(verbose_name="image", upload_to="media/", null=True)

    def __str__(self):
        return self.name
