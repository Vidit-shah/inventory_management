# Generated by Django 4.1.2 on 2022-10-29 10:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_category', models.CharField(max_length=50)),
                ('item_mrp', models.FloatField(max_length=10)),
                ('item_dp', models.FloatField(max_length=10)),
                ('item_quantity', models.IntegerField(default='1', validators=[django.core.validators.MaxValueValidator(100)])),
                ('item_desc', models.TextField(max_length=100)),
                ('item_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InventoryProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_category', models.CharField(max_length=50)),
                ('product_mrp', models.FloatField(max_length=10)),
                ('product_dp', models.FloatField(max_length=10)),
                ('product_quantity', models.IntegerField(default='1', validators=[django.core.validators.MaxValueValidator(100)])),
                ('product_desc', models.TextField(max_length=100)),
                ('product_date', models.DateField()),
            ],
        ),
    ]
