from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username

class Profile(models.Model):
    GENDER = (
        ('M', 'Homme'),
        ('F', 'Femme'),
    )
    users = models.ForeignKey(User, related_name="user_profile", on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    mobile_no = models.CharField(max_length=12)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    zip_code = models.CharField(max_length=5, blank=False, default="12345")

class Address(models.Model):
    users = models.ForeignKey(User, related_name="user_address", on_delete=models.CASCADE, null=True)
    address = models.TextField()
    mobile_no2 = models.CharField(max_length=12)