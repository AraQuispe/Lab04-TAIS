# Generated by Django 4.1.3 on 2022-12-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0007_platos_cantidad_platos_precio_product_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platos',
            name='producto',
        ),
        migrations.AddField(
            model_name='platos',
            name='producto',
            field=models.ManyToManyField(blank=True, to='e_shop.product', verbose_name='producto'),
        ),
    ]
