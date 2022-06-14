# Generated by Django 4.0.2 on 2022-06-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_century_sum_madrasa_summadrasa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='century',
            name='century',
            field=models.CharField(max_length=100, unique=True, verbose_name='Asr'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Shahar nomi'),
        ),
    ]
