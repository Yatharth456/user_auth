from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from django.utils import timezone  
from django.utils.translation import gettext_lazy as _  
from .managers import CustomUserManager 
from rest_framework.response import Response
from accounts.decorators import IsAdmin, IsManager, IsEmployee

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # These fields tie to the roles!
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee')
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
  
    username = None  
    email = models.EmailField(_('email_address'), unique=True, max_length = 200)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.CharField(choices=ROLE_CHOICES, blank=True, null=True, max_length=50) 
    date_joined = models.DateTimeField(default=timezone.now)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):  
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_staff

    # @IsManager
    # def is_manager():  
    #     "Is the user a member of manager?"  
    #     return self.is_manager 
  
    # @IsAdmin
    # def is_admin():  
    #     "Is the user as admin member?"  
    #     return self.is_admin  
  
    # @IsEmploye

    # def is_employee():  
    #     "Is the user a admin member?"  
    #     return self.is_employee
class Profile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    users = models.ForeignKey(CustomUser, related_name="user_profile", on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    mobile_no = models.CharField(max_length=12)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    zip_code = models.CharField(max_length=5, blank=False, default="12345")

class Address(models.Model):
    users = models.ForeignKey(CustomUser, related_name="user_address", on_delete=models.CASCADE, null=True)
    address = models.TextField()
    mobile_no2 = models.CharField(max_length=12)