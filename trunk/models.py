from django.db import models
from base.models import Alloma

class Subject(models.Model):
    name = models.CharField(max_length=30, verbose_name='Fan nomi')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Fanga tegishli logo')
    menu = models.ForeignKey(Alloma, on_delete=models.PROTECT, verbose_name='Fanga tegishli alloma')

    def __str__(self):
        return str(self.menu) + ' ' + str(self.name)

    class Meta:
        verbose_name = "Fan "
        verbose_name_plural = "Barcha Fanlar "

class Subject_Info(models.Model):
    text = models.TextField(verbose_name='Ma\'lumot')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Ma\'lumotga tegishli rasm')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, verbose_name='Ma\'lumot tegishli bo\'lgan Fan va Alloma')

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.text[:20]) + ' ----> ' + str(self.subject.menu.name)

    class Meta:
        verbose_name = "Fanga tegishli Ma'lumot "
        verbose_name_plural = "Fanga tegishli Ma'lumotlar "

class Subject_Extra_Info(models.Model):
    text = models.TextField(verbose_name='Ma\'lumot')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Ma\'lumotga tegishli rasm')
    subject = models.ForeignKey(Subject_Info, on_delete=models.PROTECT, verbose_name='Ma\'lumot tegishli bo\'lgan Alloma va Ma\'lumot')

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.text[:20]) + ' ----> ' + str(self.subject.subject.menu.name)

    class Meta:
        verbose_name = "Fanga tegishli Ma'lumotga aloqador Ma'lumot "
        verbose_name_plural = "Fanga tegishli Ma'lumotlarga aloqador Ma'lumotlar "


class Books(models.Model):
    name = models.CharField(max_length=100, verbose_name='Asar nomi')
    author_id = models.ForeignKey(Alloma, on_delete=models.PROTECT, verbose_name='Asar Muallifi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ilmiy Asar '
        verbose_name_plural = 'Ilmiy Asarlar '

class WoScience(models.Model):
    info = models.TextField(verbose_name='Ma\'lumot')
    image = models.ImageField(upload_to='images', verbose_name='Rasm Qo\'shish')
    author_id = models.ForeignKey(Alloma, on_delete=models.PROTECT, verbose_name='Ish Muallifi')

    def __str__(self):
        return self.info

    class Meta:
        verbose_name = 'Jahon ilm-faniga qo\'shgan hissasi '
        verbose_name_plural = 'Jahon ilm-faniga qo\'shgan hissasi '