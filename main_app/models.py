from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Option(models.Model):
    flavor = models.CharField(max_length=155)
    scoops = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.description

options = [
    Option('Strawberry', 2, 6, 'This is a great double scoop of ice cream'),
    Option('Chocolate', 3, 8, "A massive triple scoop of chocolate ice cream"),
    Option('Vanilla', 1, 4, "Boring but reliable for those who enjoy the simple things")
]

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1, related_name='orders')
    menu = models.ForeignKey(Option, on_delete=models.CASCADE, default=1, related_name='orders')
