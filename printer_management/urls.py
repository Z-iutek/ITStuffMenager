from django.contrib import admin
from django.urls import path
from core.views import (
    add_printer, 
    printer_list, 
    edit_printer, 
    delete_printer, 
    printer_detail, 
    add_equipment, 
    equipment_list, 
    edit_equipment, 
    delete_equipment, 
    user_list, 
    add_user, 
    edit_user, 
    delete_user,
    index
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page
    path('', index, name='index'),

    # Printer URLs
    path('add-printer/', add_printer, name='add_printer'),
    path('printer-list/', printer_list, name='printer_list'),
    path('edit-printer/<int:pk>/', edit_printer, name='edit_printer'),
    path('delete-printer/<int:pk>/', delete_printer, name='delete_printer'),
    path('printer-detail/<int:pk>/', printer_detail, name='printer_detail'),

    # Equipment URLs
    path('add-equipment/', add_equipment, name='add_equipment'),
    path('equipment-list/', equipment_list, name='equipment_list'),
    path('edit-equipment/<int:pk>/', edit_equipment, name='edit_equipment'),
    path('delete-equipment/<int:pk>/', delete_equipment, name='delete_equipment'),

    # User URLs
    path('user-list/', user_list, name='user_list'),
    path('add-user/', add_user, name='add_user'),
    path('edit-user/<int:pk>/', edit_user, name='edit_user'),
    path('delete-user/<int:pk>/', delete_user, name='delete_user'),
]
