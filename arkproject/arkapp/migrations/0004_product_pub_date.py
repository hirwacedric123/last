# Generated by Django 4.1.7 on 2023-03-20 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arkapp', '0003_remove_product_category_product_seller_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]