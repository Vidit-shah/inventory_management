# Generated by Django 4.1.2 on 2022-10-31 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_alter_inventoryitems_item_serial_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitems',
            name='item_category',
            field=models.CharField(choices=[('Aquaguard', 'Aquaguard'), ('Vaccum Cleaner', 'Vaccum Cleaner')], max_length=50),
        ),
        migrations.AlterField(
            model_name='inventoryproducts',
            name='product_category',
            field=models.CharField(choices=[('Aquaguard', 'Aquaguard'), ('Vaccum Cleaner', 'Vaccum Cleaner')], max_length=50),
        ),
    ]
