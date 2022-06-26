from statistics import mode
from tabnanny import verbose
from django.db import models

from trunk.models import Subject
# from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

class Regions(models.Model):
    name = models.CharField(max_length=50, verbose_name='Shahar nomi', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shahar "
        verbose_name_plural = "Shaharlar "

class Century(models.Model):
    century = models.CharField(max_length=100, verbose_name='Asr', unique=True)

    def __str__(self) -> str:
        return self.century

    class Meta:
        verbose_name = "Asr "
        verbose_name_plural = "Asrlar "

class SumMadrasa(models.Model):
    region_id = models.ForeignKey(Regions, null=True, on_delete=models.CASCADE, verbose_name='Shahar ')
    century_id = models.ForeignKey(Century, null=True, on_delete=models.CASCADE, verbose_name='Asr ')
    sum_madrasa = models.CharField(max_length=100, null=True, verbose_name='Madrasalar soni ')

    def __str__(self) -> str:
        return self.sum_madrasa

    class Meta:
        verbose_name = "Madrasalar soni "
        verbose_name_plural = "Madrasalar soni "


class MadrasaName(models.Model):
    name = models.CharField(max_length=100, verbose_name='Madrasa nomi', unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Madrasa nomi '
        verbose_name_plural = 'Madrasalar nomlari '


class Madrasa(models.Model):
    madrasa_id = models.ForeignKey(MadrasaName, on_delete=models.CASCADE, verbose_name='Madrasa', null=True)
    century_id = models.ForeignKey(Century, on_delete=models.PROTECT, verbose_name='Madrasa mavjud bo\'lgan asr')
    region_id = models.ForeignKey(Regions, null=True, on_delete=models.PROTECT, verbose_name='Madrasa joylashgan shahar')

    def __str__(self) -> str:
        return str(self.region_id.name) + ' -- ' + str(self.century_id.century) + ' ' + str(self.madrasa_id.name)

    class Meta:
        verbose_name = "Madrasa "
        verbose_name_plural = "Barcha Madrasalar "

class AllomaMenu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Menyu nomi')
    logo = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Alloma Tarmoq Menyusi "
        verbose_name_plural = "Alloma Tarmoqlar Menyulari "

# def nameImage(instance, imagename):
#     return '/'.join(['images', str(instance.name), imagename])

class Books(models.Model):
    name = models.CharField(max_length=100, verbose_name='Asar nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ilmiy Asar '
        verbose_name_plural = 'Ilmiy Asarlar '

class Alloma(models.Model):
    name = models.CharField(max_length=50, verbose_name='Alloma ismi')
    birth_year = models.CharField(max_length=30, null=True, verbose_name='Tug\'ilgan yili')
    birth_area = models.CharField(max_length=50, null=True, verbose_name='Tug\'ilgan joyi')
    image = models.ImageField(upload_to='images', verbose_name='Allomaning rasmi')
    madrasa_alloma = models.ForeignKey(Madrasa, on_delete=models.PROTECT, verbose_name='Alloma mansub madrasa')
    about = models.TextField(null=True, verbose_name='Alloma haqida ma\'lumot')
    subject_id = models.ManyToManyField(Subject, blank=True, verbose_name='Fanlar')
    books = models.ManyToManyField(Books, blank=True, verbose_name='Yozgan asarlari')
    allomamenu = models.ManyToManyField(AllomaMenu, blank=True, verbose_name='Allomaga tegishli yo\'nalishlar')

    def __str__(self) -> str:
        return self.name 

    class Meta:
        verbose_name = "Alloma "
        verbose_name_plural = "Allomalar "


class Subject_Info(models.Model):
    text = models.TextField(verbose_name='Ma\'lumot')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Ma\'lumotga tegishli rasm')
    alloma_id = models.ForeignKey(Alloma, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Ma\'lumot tegishli bo\'lgan Alloma')
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Ma\'lumot tegishli bo\'lgan Fan')

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.text[:20]) + ' ----> ' + str(self.subject_id.name)

    class Meta:
        verbose_name = "Fanga tegishli Ma'lumot "
        verbose_name_plural = "Fanga tegishli Ma'lumotlar "


class Subject_Extra_Info(models.Model):
    text = models.TextField(verbose_name='Ma\'lumot')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Ma\'lumotga tegishli rasm')
    subject = models.ForeignKey(Subject_Info, on_delete=models.PROTECT, verbose_name='Ma\'lumot tegishli bo\'lgan Alloma va Ma\'lumot')

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.text[:20]) + ' ----> ' + str(self.subject.alloma_id.name)

    class Meta:
        verbose_name = "Fanga tegishli Ma'lumotga aloqador Ma'lumot "
        verbose_name_plural = "Fanga tegishli Ma'lumotlarga aloqador Ma'lumotlar "


class WoScience(models.Model):
    info = models.TextField(verbose_name='Ma\'lumot')
    image = models.ImageField(upload_to='images', verbose_name='Rasm Qo\'shish')
    author_id = models.ForeignKey(Alloma, on_delete=models.PROTECT, verbose_name='Ish Muallifi')

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = 'Jahon ilm-faniga qo\'shgan hissasi '
        verbose_name_plural = 'Jahon ilm-faniga qo\'shgan hissasi '