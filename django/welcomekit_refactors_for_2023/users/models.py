# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .choice import *

class UserManager(BaseUserManager):

    def create_user(self, user_id, password,
                    name, department, grade, track,
                    leader, student1, student2, student3,
                    **extra_fields):
          
        user = self.model(
            user_id = user_id,              # 아이디

            name = name,                    # 이름
            department = department,        # 학과
            grade = grade,                  # 학년
            track = track,                  # 트랙
            leader = leader,                # 팀장

            student1 = student1,                # 팀원1
            student2 = student2,                # 팀원2
            student3 = student3,                # 팀원3

            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user_id, password,
                         name=None, department=None, grade=None, track=None,
                         leader=None, student1=None, student2=None, student3=None
                         ):
        
        user = self.create_user(
            user_id, password,
            name, department, grade, track,
            leader, student1, student2, student3)
        
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
    department = models.CharField(max_length=24, verbose_name="학과", null=True)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=18, verbose_name="학년", null=True)
    track = models.CharField(choices=TRACK_CHOICES, max_length=18, verbose_name="트랙", null=True)

    leader = models.CharField(max_length=8, verbose_name="팀장", null=True)
    student1 = models.CharField(max_length=8, verbose_name="팀원1", null=True)
    student2 = models.CharField(max_length=8, verbose_name="팀원2", null=True)
    student3 = models.CharField(max_length=8, verbose_name="팀원3", null=True, blank=True)


    level = models.CharField(choices=LEVEL_CHOICES, max_length=5, verbose_name="등급", default=2)

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

class TeamManager(models.Model):
    
    tm = models.TextField(verbose_name='팀장', null=True, blank=True)
    src = models.TextField(verbose_name='이미지주소', null=True, blank=True)
    hi = models.TextField(verbose_name='좌우명', null=True, blank=True)
    email = models.TextField(verbose_name='연락처', null=True, blank=True)
    department = models.TextField(verbose_name='학과', null=True, blank=True)


    def __str__(self):
        return str(self.tm)

    class Meta:
        db_table = '팀장소개'
        verbose_name = '팀장소개'
        verbose_name_plural = '팀장소개'