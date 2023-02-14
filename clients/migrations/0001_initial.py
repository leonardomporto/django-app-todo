# Generated by Django 3.2.16 on 2023-02-08 01:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('nikname', models.CharField(max_length=255, verbose_name='Nome de Usuário')),
                ('password', models.CharField(max_length=255, verbose_name='Senha')),
                ('birthday', models.DateField()),
                ('date_payment', models.DateField()),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]
