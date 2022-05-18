from django.contrib import admin
from django.db import models
from accounts.models import  User 
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


    
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
                "Personal info",
                {"fields": ("picture", "pseudo","role", "warehouse", "notes")},
        ),
        (
                "Permissions",
                {
                  "fields":(
                            "is_active",
                            "is_staff",
                            "is_manager",
                            "is_superuser",
                            "groups",
                            "user_permissions",
         )
                },
                ),
                (
                "Important dates",
                {"fields": ("last_login", "date_joined")},
                ),
                )
    add_fieldsets = (
                (
                None,
                {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
                },
                ),
                )

    list_display = (
                "email",
                "warehouse", 
                "pseudo", 
                "role",
                "is_staff",
                "is_active"
                )
    search_fields = ("email", "picture", "pseudo","role" )
    ordering = ("email"),
                                            
admin.site.register(User, UserAdmin) 
