# Generated by Django 2.2 on 2019-11-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_ratting',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True),
        ),
    ]