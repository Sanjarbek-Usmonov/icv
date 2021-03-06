# Generated by Django 4.0.2 on 2022-06-26 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trunk', '0009_remove_subject_info_subject_and_more'),
        ('base', '0018_alloma_subject_id_woscience_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='author_id',
        ),
        migrations.AddField(
            model_name='alloma',
            name='books',
            field=models.ManyToManyField(blank=True, to='base.Books', verbose_name='Yozgan asarlari'),
        ),
        migrations.AlterField(
            model_name='alloma',
            name='subject_id',
            field=models.ManyToManyField(blank=True, to='trunk.Subject', verbose_name='Fanlar'),
        ),
        migrations.CreateModel(
            name='Subject_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name="Ma'lumot")),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name="Ma'lumotga tegishli rasm")),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.alloma', verbose_name="Ma'lumot tegishli bo'lgan Fan va Alloma")),
            ],
            options={
                'verbose_name': "Fanga tegishli Ma'lumot ",
                'verbose_name_plural': "Fanga tegishli Ma'lumotlar ",
            },
        ),
        migrations.CreateModel(
            name='Subject_Extra_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name="Ma'lumot")),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name="Ma'lumotga tegishli rasm")),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.subject_info', verbose_name="Ma'lumot tegishli bo'lgan Alloma va Ma'lumot")),
            ],
            options={
                'verbose_name': "Fanga tegishli Ma'lumotga aloqador Ma'lumot ",
                'verbose_name_plural': "Fanga tegishli Ma'lumotlarga aloqador Ma'lumotlar ",
            },
        ),
    ]
