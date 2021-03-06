from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .choice import *

class UserManager(BaseUserManager):
    def create_user(self, user_id, password, name, modifier, department, grade, track, leader, value, interest, student1, student1_intro, student1_value1, student1_value2, student1_value3, student2, student2_intro, student2_value1, student2_value2, student2_value3, **extra_fields):
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
            student1_value1 = student1_value1,
            student1_value2 = student1_value2,
            student1_value3 = student1_value3,

            student2 = student2,
            student2_intro = student2_intro,
            student2_value1 = student2_value1,
            student2_value2 = student2_value2,
            student2_value3 = student2_value3,

            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, name=None, modifier=None, department=None, grade=None, track=None, leader=None, value=None, interest=None, student1=None, student1_intro=None, student1_value1=None, student1_value2=None, student1_value3=None ,student2=None, student2_intro=None,  student2_value1=None, student2_value2=None, student2_value3=None ):
        user = self.create_user(user_id, password, name, modifier, department, grade, track, leader, value, interest,  student1, student1_intro, student1_value1, student1_value2, student1_value3, student2, student2_intro, student2_value1, student2_value2, student2_value3)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    
    objects = UserManager()

    user_id = models.CharField(max_length=17, verbose_name="?????????", unique=True)
    password = models.CharField(max_length=256, verbose_name="????????????")
    name = models.CharField(max_length=8, verbose_name="??????", null=True)
    modifier = models.CharField(max_length=16, verbose_name="?????????", null=True)
    department = models.CharField(max_length=24, verbose_name="??????", null=True)
    grade = models.CharField(choices=GRADE_CHOICES, max_length=18, verbose_name="??????", null=True)
    track = models.CharField(choices=TRACK_CHOICES, max_length=18, verbose_name="??????", null=True)
    leader = models.CharField(max_length=8, verbose_name="??????", null=True)
    value = models.CharField(max_length=8, verbose_name="??????", null=True)
    interest = models.CharField(max_length=8, verbose_name="?????????", null=True)
    level = models.CharField(choices=LEVEL_CHOICES, max_length=18, verbose_name="??????", default=2)

    student1 = models.CharField(max_length=8, verbose_name="??????1", null=True)
    student1_intro = models.TextField(max_length=256, verbose_name="??????1 ??????", null=True)
    student1_value1 = models.CharField(max_length=8, verbose_name="??????1 ??????1", null=True)
    student1_value2 = models.CharField(max_length=8, verbose_name="??????1 ??????2", null=True)
    student1_value3 = models.CharField(max_length=8, verbose_name="??????1 ??????3", null=True)

    student2 = models.CharField(max_length=8, verbose_name="??????2", null=True)
    student2_intro = models.TextField(max_length=256, verbose_name="??????2 ??????", null=True)
    student2_value1 = models.CharField(max_length=8, verbose_name="??????2 ??????1", null=True)
    student2_value2 = models.CharField(max_length=8, verbose_name="??????2 ??????2", null=True)
    student2_value3 = models.CharField(max_length=8, verbose_name="??????2 ??????3", null=True)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    
    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "????????????"
        verbose_name = "?????????"
        verbose_name_plural = "?????????"