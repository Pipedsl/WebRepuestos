# Generated by Django 4.1.7 on 2023-06-26 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0009_proveedor_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='categoria',
        ),
    ]
