from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=30, verbose_name='Fan nomi')
    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Fanga tegishli logo')
    # menu = models.ForeignKey(Alloma, on_delete=models.PROTECT, verbose_name='Fanga tegishli alloma')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Fan "
        verbose_name_plural = "Barcha Fanlar "






