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
        fields = ['type', 'model', 'serial_number', 'condition', 'assigned_to']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role']  # Dopasowane do modelu User
