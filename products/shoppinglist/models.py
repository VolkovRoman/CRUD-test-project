from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()

    objects = models.Manager

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return '/update/{}/'.format(self.id)
