# Generated by Django 2.2 on 2020-02-06 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('post_code', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('post_code', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_conatct', models.CharField(max_length=15)),
                ('customer_email', models.EmailField(max_length=254)),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.BillingAddress')),
                ('buying_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.ShippingAddress')),
            ],
        ),
    ]
