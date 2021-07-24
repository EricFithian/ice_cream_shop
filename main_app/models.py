from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Menu(models.Model):
    flavor = models.CharField(max_length=155)
    scoops = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.description

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1, related_name='orders')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=1, related_name='orders')
