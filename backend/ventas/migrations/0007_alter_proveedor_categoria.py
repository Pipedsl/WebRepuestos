# Generated by Django 4.1.7 on 2023-06-25 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_venta_remove_cliente_papellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='categoria',
            field=models.CharField(blank=True, choices=[('accesorios', 'Accesorios'), ('carroceria', 'Carroceria'), ('motor', 'Motor')], max_length=10, null=True),
        ),
    ]