# Generated by Django 4.0.2 on 2022-02-21 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_alloma_about_alter_alloma_allomamenu_and_more'),
        ('trunk', '0002_alter_subject_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Fanga tegishli logo'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.alloma', verbose_name='Fanga tegishli alloma'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Fan nomi'),
        ),
        migrations.AlterField(
            model_name='subject_extra_info',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name="Ma'lumotga tegishli rasm"),
        ),
        migrations.AlterField(
            model_name='subject_extra_info',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trunk.subject_info', verbose_name="Ma'lumot tegishli bo'lgan Alloma va Ma'lumot"),
        ),
        migrations.AlterField(
            model_name='subject_extra_info',
            name='text',
            field=models.TextField(verbose_name="Ma'lumot"),
        ),
        migrations.AlterField(
            model_name='subject_info',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name="Ma'lumotga tegishli rasm"),
        ),
        migrations.AlterField(
            model_name='subject_info',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trunk.subject', verbose_name="Ma'lumot tegishli bo'lgan Fan va Alloma"),
        ),
        migrations.AlterField(
            model_name='subject_info',
            name='text',
            field=models.TextField(verbose_name="Ma'lumot"),
        ),
    ]
