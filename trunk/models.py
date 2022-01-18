from django.db import models
from base.models import Alloma

class Subject(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    menu = models.ForeignKey(Alloma, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.menu) + ' ' + str(self.name)

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Barcha Fanlar"

class Subject_Info(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.text[:20]) + ' ----> ' + str(self.subject.menu.name)

    class Meta:
        verbose_name = "Fanga tegishli Ma'lumot"
        verbose_name_plural = "Fanga tegishli Ma'lumotlar"

class Subject_Extra_Info(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    subject = models.ForeignKey(Subject_Info, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.text[:20]) + ' ----> ' + str(self.subject.subject.menu.name)

    class Meta:
        verbose_name = "Fanga tegishli Ma'lumotga aloqador Ma'lumot"
        verbose_name_plural = "Fanga tegishli Ma'lumotlarga aloqador Ma'lumotlar"
