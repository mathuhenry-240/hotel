from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Rooms(models.Model):
    room_name = models.CharField(max_length=50)
    room_available_for = models.IntegerField()
    room_type = models.CharField(max_length=50)
    room_charges = models.DecimalField(max_digits=7, decimal_places=2)
    Isvaccant = models.BooleanField(default=True)


class Customers(models.Model):
    cust_no = models.CharField(max_length=20)  # hot/2020/1
    First_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    Email = models.EmailField()

    # phone number regular expression
    phone_number_validator = RegexValidator(regex=r'^(0|\+)\d{8,15}$')

    Phone_Number = models.CharField(validators=[phone_number_validator], max_length=17, unique=True)
    bookedOn = models.DateTimeField(auto_now_add=True)
    Cleared = models.BooleanField(default=False)


class Bookings(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    bookerOn = models.DateTimeField(auto_now_add=True)
    expired = models.BooleanField(default=False)
