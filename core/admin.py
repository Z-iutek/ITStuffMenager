from django.contrib import admin
from .models import Printer, PrinterLog, User, Equipment

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'hostname', 'model', 'status')

@admin.register(PrinterLog)
class PrinterLogAdmin(admin.ModelAdmin):
    list_display = ('printer', 'date_logged', 'total_prints', 'scans')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'department')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('type', 'model', 'serial_number', 'condition', 'assigned_to')
