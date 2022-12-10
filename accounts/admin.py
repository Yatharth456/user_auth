from django.contrib import admin
from django.contrib.auth import authenticate  
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):    
    model = CustomUser  
  
    list_display = ('email', 'is_active',)  
    list_filter = ('email', 'is_active',)  
    fieldsets = (  
        (None, {'fields': ('email', 'password')}),  
        ('Permissions', {'fields': ('is_staff', 'is_active')}),  
    )  
    add_fieldsets = (  
        (None, {  
            'classes': ('wide',),  
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}  
        ),  
    )  
    search_fields = ('email',)  
    ordering = ('email',)  
    filter_horizontal = ()  
  
admin.site.register(CustomUser, CustomUserAdmin)  