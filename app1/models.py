from django.db import models


class App1(models.Model):
    name = models.CharField('名字', max_length=50)

    class Meta:
        verbose_name = verbose_name_plural = '应用1'

    def __str__(self):
        return self.name
