from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100, default='Untitled')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)

class Menu(models.Model):
    name = models.CharField(max_length=200, default='Untitled')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name} : {str(self.price)}'
#    def __str__(self):
#        return self.name


class Booking(models.Model):
    customer_name = models.CharField(max_length=200)
    booking_date = models.DateTimeField()
    number_of_guests = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_date}"