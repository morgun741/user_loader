from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Course(models.Model):
    course_name = models.CharField(verbose_name='choice', max_length=64, unique=True)
    short_name = models.TextField(verbose_name='shortly', blank=True)

class User(AbstractUser):
    course = models.ForeignKey(Course, on_delete=models.PROTECT, null=True, blank=True)
