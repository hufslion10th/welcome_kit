import os
from django.conf import settings
from django.db import models

class Greet(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아기사자')
    content_k = models.TextField(verbose_name='고도희')
    content_h = models.TextField(verbose_name='홍예은')
    content_s = models.TextField(verbose_name='설희관')
    content_p = models.TextField(verbose_name='박경준')
    content_m = models.TextField(verbose_name='민선아')
    content_j = models.TextField(verbose_name='정지원')
    content_c = models.TextField(verbose_name='정우진')

    def __str__(self):
        return self.name

    class Meta:
        db_table = '롤링페이퍼'
        verbose_name = '롤링페이퍼'
        verbose_name_plural = '롤링페이퍼'