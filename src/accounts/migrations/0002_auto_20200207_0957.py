# Generated by Django 2.2 on 2020-02-07 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='shipping_address',
        ),
        migrations.DeleteModel(
            name='BiliingAddress',
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
