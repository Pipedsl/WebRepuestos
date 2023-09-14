# Generated by Django 4.1.7 on 2023-07-10 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0011_proveedor_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(through='ventas.ItemCarrito', to='ventas.producto'),
        ),
    ]
