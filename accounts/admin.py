from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
# admin.site.unregister(User)
admin.site.register(User, UserAdmin)