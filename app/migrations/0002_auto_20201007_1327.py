# Generated by Django 3.1 on 2020-10-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unitprice',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=8),
        ),
    ]
