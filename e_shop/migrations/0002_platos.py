# Generated by Django 4.1.3 on 2022-11-22 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_shop.project')),
            ],
        ),
    ]
