from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model): #запоминаем поступок
    title = models.CharField('ФИО', max_length=50)
    boy_age = models.CharField('18', max_length=50)
    score = models.CharField('10', max_length=50)
    task = models.TextField('проступок')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'проступок'
        verbose_name_plural = 'проступки'