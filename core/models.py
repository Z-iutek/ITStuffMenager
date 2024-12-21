from django.db import models

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

    from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    EQUIPMENT_TYPE_CHOICES = [
        ('laptop', 'Laptop'),
        ('monitor', 'Monitor'),
        ('phone', 'Phone'),
        ('other', 'Other'),
    ]

    type = models.CharField(max_length=50, choices=EQUIPMENT_TYPE_CHOICES)
    model = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    condition = models.CharField(max_length=50, default='new')  # new, used, damaged
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='equipment')
    assigned_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} - {self.model} ({self.serial_number})"