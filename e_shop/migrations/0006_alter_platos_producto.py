# Generated by Django 4.1.3 on 2022-11-22 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0005_alter_platos_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='e_shop.product'),
        ),
    ]
