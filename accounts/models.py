from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from django.utils import timezone  
from django.utils.translation import gettext_lazy as _  
from .managers import CustomUserManager 

class CustomUser(AbstractBaseUser, PermissionsMixin):  
    username = None  
    email = models.EmailField(_('email_address'), unique=True, max_length = 200)  
    date_joined = models.DateTimeField(default=timezone.now)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []
  
    objects = CustomUserManager()  
      
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def is_staff(self):  
        "Is the user a member of staff?"  
        return self.is_staff  
  
    @property  
    def is_admin(self):  
        "Is the user a admin member?"  
        return self.is_admin  
  
    def __str__(self):  
        return self.email  

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