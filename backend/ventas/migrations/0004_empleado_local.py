# Generated by Django 4.1.7 on 2023-06-23 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_cliente_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='local',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
