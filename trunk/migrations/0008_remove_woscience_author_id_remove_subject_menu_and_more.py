# Generated by Django 4.0.2 on 2022-06-25 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trunk', '0007_rename_author_woscience_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='woscience',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='menu',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='WoScience',
        ),
    ]
