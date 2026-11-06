from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.Name


class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    def __init__(self, *args, **kwargs):
        if 'title' in kwargs:
            kwargs.setdefault('Title', kwargs.pop('title'))
        if 'price' in kwargs:
            kwargs.setdefault('Price', kwargs.pop('price'))
        if 'inventory' in kwargs:
            kwargs.setdefault('Inventory', kwargs.pop('inventory'))
        super().__init__(*args, **kwargs)

    @property
    def title(self):
        return self.Title

    @title.setter
    def title(self, value):
        self.Title = value

    @property
    def price(self):
        return self.Price

    @price.setter
    def price(self, value):
        self.Price = value

    @property
    def inventory(self):
        return self.Inventory

    @inventory.setter
    def inventory(self, value):
        self.Inventory = value

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'



MenuItem = Menu


