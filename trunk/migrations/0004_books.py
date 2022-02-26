# Generated by Django 4.0.2 on 2022-02-26 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_alloma_allomamenu_alter_regions_name'),
        ('trunk', '0003_alter_subject_image_alter_subject_menu_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Asar nomi')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.alloma', verbose_name='Asar Muallifi')),
            ],
            options={
                'verbose_name': 'Ilmiy Asar',
                'verbose_name_plural': 'Ilmiy Asarlar',
            },
        ),
    ]
