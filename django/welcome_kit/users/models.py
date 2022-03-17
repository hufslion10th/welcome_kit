from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .choice import *

class UserManager(BaseUserManager):
    def create_user(self, user_id, password, name, modifier, department, grade, track, leader, value, interest, student1, student1_intro, student2, student2_intro, **extra_fields):
        user = self.model(
            user_id = user_id,
            name = name,
            modifier = modifier,
            department = department,
            grade = grade,
            track = track,
            leader = leader,
            value = value,
            interest = interest,
            student1 = student1,
            student1_intro = student1_intro,
            student2 = student2,
            student2_intro = student2_intro,

            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, name=None, modifier=None, department=None, grade=None, track=None, leader=None, value=None, interest=None, student1=None, student1_intro=None, student2=None, student2_intro=None):
        user = self.create_user(user_id, password, name, modifier, department, grade, track, leader, value, interest,  student1, student1_intro, student2, student2_intro)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    
    objects = UserManager()

    user_id = models.CharField(max_length=17, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    name = models.CharField(max_length=8, verbose_name="이름", null=True)
    modifier = models.CharField(max_length=8, verbose_name="수식어", null=True)
    department = models.CharField(max_length=24, verbose_name="학과", null=True)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=18, verbose_name="학년", null=True)
    track = models.CharField(choices=TRACK_CHOICES, max_length=18, verbose_name="트랙", null=True)
    leader = models.CharField(max_length=8, verbose_name="리더", null=True)
    value = models.CharField(max_length=8, verbose_name="가치", null=True)
    interest = models.CharField(max_length=8, verbose_name="관심사", null=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="등급", default=2)

    student1 = models.CharField(max_length=8, verbose_name="추천1", null=True)
    student1_intro = models.TextField(max_length=256, verbose_name="추천1 설명", null=True)
    student2 = models.CharField(max_length=8, verbose_name="추천2", null=True)
    student2_intro = models.TextField(max_length=256, verbose_name="추천2 설명", null=True)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    
    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "회원목록"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"