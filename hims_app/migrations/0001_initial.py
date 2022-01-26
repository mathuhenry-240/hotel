# Generated by Django 3.2.9 on 2021-12-07 22:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_no', models.CharField(max_length=20)),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Surname', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(regex='^(0|\\+)\\d{8,15}$')])),
                ('bookedOn', models.DateTimeField(auto_now_add=True)),
                ('Cleared', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=50)),
                ('room_available_for', models.IntegerField()),
                ('room_type', models.CharField(max_length=50)),
                ('room_charges', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Isvaccant', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookerOn', models.DateTimeField(auto_now_add=True)),
                ('expired', models.BooleanField(default=False)),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hims_app.customers')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hims_app.rooms')),
            ],
        ),
    ]
