# Generated by Django 2.2 on 2020-02-03 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20200203_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=19),
        ),
    ]