from django.db import models


class Tasks(models.Model):
    title = models.CharField('ФИО', max_length=50)
    task = models.TextField('проступок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'проступок'
        verbose_name_plural = 'проступки'
