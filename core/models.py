from django.db import models
from django.contrib.auth.models import User

class Printer(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    hostname = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    mac_address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default='Unknown')

    def __str__(self):
        return f"{self.hostname} ({self.ip_address})"

class PrinterLog(models.Model):
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE, related_name='logs')
    date_logged = models.DateTimeField(auto_now_add=True)
    black_and_white_prints = models.IntegerField(null=True, blank=True)
    color_prints = models.IntegerField(null=True, blank=True)
    total_prints = models.IntegerField(null=True, blank=True)
    scans = models.IntegerField(null=True, blank=True)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Employee', 'Employee')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Equipment(models.Model):
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    condition = models.CharField(max_length=50)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.type} - {self.model} ({self.serial_number})"
    

