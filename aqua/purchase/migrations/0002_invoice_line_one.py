# Generated by Django 4.1.2 on 2022-11-01 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_delete_checkout_delete_checkoutitems'),
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='line_one',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.inventoryproducts'),
        ),
    ]
