from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    course = models.ForeignKey(Course, blank=True, null=True)
    last_name = models.CharField(verbose_name='last_name', )

class Course(models.Model):
