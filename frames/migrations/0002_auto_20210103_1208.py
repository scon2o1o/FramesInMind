# Generated by Django 3.1.4 on 2021-01-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
