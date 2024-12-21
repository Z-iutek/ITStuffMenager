from django import forms
from .models import Printer
from .models import User
from .models import Equipment
class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['ip_address', 'hostname', 'model', 'serial_number', 'mac_address', 'status']


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['type', 'model', 'serial_number', 'condition', 'assigned_to', 'assigned_date', 'return_date', 'notes']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'position', 'department']  # Dopasowane do modelu User
