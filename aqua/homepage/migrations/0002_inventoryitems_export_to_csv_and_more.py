# Generated by Django 4.1.2 on 2022-10-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitems',
            name='export_to_csv',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='inventoryproducts',
            name='export_to_csv',
            field=models.BooleanField(default=True),
        ),
    ]
