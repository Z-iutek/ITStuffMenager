from django.shortcuts import render, redirect, get_object_or_404
from .forms import PrinterForm
from .models import Printer, PrinterLog
from .models import User
from .models import Equipment
from .forms import UserForm
from .forms import EquipmentForm

import subprocess

# View to add a new printer
def add_printer(request):
    if request.method == 'POST':
        form = PrinterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('printer_list')  # Redirect to a list of printers after saving
    else:
        form = PrinterForm()
    return render(request, 'core/add_printer.html', {'form': form})

# View to list all printers
def printer_list(request):
    printers = Printer.objects.all()
    return render(request, 'core/printer_list.html', {'printers': printers})

# View to edit a printer
def edit_printer(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    if request.method == 'POST':
        form = PrinterForm(request.POST, instance=printer)
        if form.is_valid():
            form.save()
            return redirect('printer_list')
    else:
        form = PrinterForm(instance=printer)
    return render(request, 'core/edit_printer.html', {'form': form})

# View to delete a printer
def delete_printer(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    if request.method == 'POST':
        printer.delete()
        return redirect('printer_list')
    return render(request, 'core/delete_printer.html', {'printer': printer})

# View to show printer details and fetch SNMP data
def printer_detail(request, pk):
    from itertools import chain

    printer = get_object_or_404(Printer, pk=pk)
    snmp_data = {}

    # Mapowanie zmiennych do ich głównych i alternatywnych OID
    oid_map = {
        "Model": [".1.3.6.1.4.1.1602.1.1.1.1.0"],
        "Serial Number": [".1.3.6.1.4.1.1602.1.2.1.8.1.3.1.1"],
        "Wydruki Czarno Białe": [
            ".1.3.6.1.4.1.1602.1.11.1.3.1.4.109",
            ".1.3.6.1.4.1.1602.1.11.2.1.1.3.5",
            ".1.3.6.1.2.1.43.10.2.1.4.1.1",
        ],
        "Wydruki kolorowe": [
            ".1.3.6.1.4.1.1602.1.11.1.4.1.4.123",
            ".1.3.6.1.4.1.1602.1.11.2.1.1.3.3",
        ],
        "Suma wydruków": [
            ".1.3.6.1.4.1.1602.1.11.1.4.1.4.101",
            ".1.3.6.1.4.1.1602.1.11.2.1.1.3.1",
        ],
        "Suma skanów": [".1.3.6.1.4.1.1602.1.11.1.4.1.4.501"],
    }

    if request.method == "POST":
        for key, oids in oid_map.items():
            success = False
            for oid in oids:
                try:
                    # Uruchomienie komendy SNMP dla danego OID
                    snmp_output = subprocess.check_output(
                        [
                            "C:/Tools/SnmpGet.exe",
                            "-c:public",
                            f"-r:{printer.ip_address}",
                            f"-o:{oid}",
                        ],
                        universal_newlines=True,
                    ).strip()

                    # Wyciągnięcie wartości z wyniku
                    for line in snmp_output.splitlines():
                        if "Value=" in line:
                            snmp_data[key] = line.split("Value=")[-1].strip()
                            success = True
                            break

                    # Jeśli dane zostały pobrane, nie próbuj alternatywnych OID
                    if success:
                        break
                except subprocess.CalledProcessError as e:
                    snmp_data[key] = f"Błąd SNMP: {e.returncode}"
                except FileNotFoundError:
                    snmp_data[key] = "Nie znaleziono SnmpGet.exe. Sprawdź konfigurację PATH."
                except Exception as e:
                    snmp_data[key] = f"Błąd: {str(e)}"

            # Jeśli żaden OID nie zwrócił wartości
            if not success:
                snmp_data[key] = "Brak danych lub nieobsługiwany model drukarki"

    return render(request, "core/printer_detail.html", {"printer": printer, "snmp_data": snmp_data})

def user_list(request):
    users = User.objects.all()
    return render(request, 'core/user_list.html', {'users': users})


def add_user(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'core/add_user.html', {'form': form})
def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'core/add_equipment.html', {'form': form})


def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipment': equipment})


def edit_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'core/edit_equipment.html', {'form': form})

def delete_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')
    return render(request, 'core/delete_equipment.html', {'equipment': equipment})

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'core/edit_user.html', {'form': form})

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'core/delete_user.html', {'user': user})
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'core/delete_user.html', {'user': user})

def index(request):
    return render(request, 'core/index.html')
