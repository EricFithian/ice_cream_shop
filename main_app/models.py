from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Menu_Items(models.Model):
    flavor = models.CharField(max_length=155)
    scoops = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.flavor

class Test_Items:
    def __init__(self, flavor, scoops, price, description):
        self.flavor = flavor
        self.scoops = scoops
        self.price = price
        self.description = description

menu = [
    Test_Items('Strawberry', 2, 6, 'This is a great double scoop of ice cream'),
    Test_Items('Chocolate', 3, 8, "A massive triple scoop of chocolate ice cream"),
    Test_Items('Vanilla', 1, 4, "Boring but reliable for those who enjoy the simple things")
]

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1, related_name='orders')
    menu = models.ForeignKey(Menu_Items, on_delete=models.CASCADE, default=1, related_name='orders')
