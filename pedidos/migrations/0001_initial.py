# Generated by Django 5.1.3 on 2024-11-25 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('producto', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('realizado', 'Realizado')], max_length=20)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
