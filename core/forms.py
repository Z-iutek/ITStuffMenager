from django import forms
from .models import Printer
from .models import Employee
from .models import Equipment
class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['ip_address', 'hostname', 'model', 'serial_number', 'mac_address', 'status']


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['type', 'model', 'serial_number', 'condition', 'assigned_to']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'role']  # Dopasowane do modelu Employee

class CSVImportForm(forms.Form):
    MODEL_CHOICES = [
        ('equipment', 'Equipment'),
        ('user', 'Employee'),
        ('printer', 'Printer'),
    ]
    model = forms.ChoiceField(choices=MODEL_CHOICES, label="Model to import into")
    csv_file = forms.FileField(label="Select a CSV file")
