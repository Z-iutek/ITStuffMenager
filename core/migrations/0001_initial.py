# Generated by Django 5.1.4 on 2024-12-20 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(unique=True)),
                ('hostname', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=255, null=True)),
                ('mac_address', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(default='Unknown', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PrinterLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_logged', models.DateTimeField(auto_now_add=True)),
                ('black_and_white_prints', models.IntegerField(blank=True, null=True)),
                ('color_prints', models.IntegerField(blank=True, null=True)),
                ('total_prints', models.IntegerField(blank=True, null=True)),
                ('scans', models.IntegerField(blank=True, null=True)),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='core.printer')),
            ],
        ),
    ]
