from django.conf import settings
from django.db import models


class Greet(models.Model):
    '''
    아기사자들에게 전해주는 운영진들의
    축하 메세지를 위한 롤링페이퍼 모델입니다.
    '''
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='아기사자')

    kim = models.TextField(verbose_name='김강민', null=True, blank=True)
    one = models.TextField(verbose_name='원동현', null=True, blank=True)
    min = models.TextField(verbose_name='조민솔', null=True, blank=True)
    cho = models.TextField(verbose_name='조성민', null=True, blank=True)
    win = models.TextField(verbose_name='최승호', null=True, blank=True)
    yes = models.TextField(verbose_name='임예람', null=True, blank=True)
    cwj = models.TextField(verbose_name='정우진', null=True, blank=True)
    kyk = models.TextField(verbose_name='김윤경', null=True, blank=True)
    sim = models.TextField(verbose_name='심재성', null=True, blank=True)
    cha = models.TextField(verbose_name='김재우', null=True, blank=True)
    hye = models.TextField(verbose_name='홍예은', null=True, blank=True)
    kye = models.TextField(verbose_name='김예은', null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = '롤링페이퍼'
        verbose_name = '롤링페이퍼'
        verbose_name_plural = '롤링페이퍼'