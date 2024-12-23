from django.contrib import admin
from .models import Printer, PrinterLog, User, Equipment

@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'hostname', 'model', 'status')

@admin.register(PrinterLog)
class PrinterLogAdmin(admin.ModelAdmin):
    list_display = ('printer', 'date_logged', 'total_prints', 'scans')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('type', 'model', 'serial_number', 'condition', 'assigned_to')

from django.contrib import admin
from .models import Employee  # Importuj model Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role')
