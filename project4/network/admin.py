from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class Info(admin.ModelAdmin):
    fields = [
        'phoneNumber',
        'accountKey',
        'firstName',
        'lastName',
        'email',
        'nric',
    ]

admin.site.register(User, Info)