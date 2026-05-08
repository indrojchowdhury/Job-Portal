from django.db import models
from django.contrib.auth.models import AbstractUser

# Creating a custom user model to handle two types of users
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('seeker', 'Job Seeker'),
        ('employer', 'Employer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='seeker')

    def __str__(self):
        return self.username
