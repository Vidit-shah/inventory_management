# Generated by Django 4.1.2 on 2022-10-31 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_checkout_cost_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitems',
            name='item_HSN',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='inventoryitems',
            name='item_serial',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='inventoryproducts',
            name='product_HSN',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='inventoryproducts',
            name='product_serial',
            field=models.CharField(default=True, max_length=50),
        ),
    ]