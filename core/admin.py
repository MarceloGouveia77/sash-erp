from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User
# Register your models here.



ADDITIONAL_USER_FIELDS = (
    ('api_token',{'fields' : ('token',)}),
    
)

class MyUserAdmin(UserAdmin):

    model = User

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

admin.site.register(User,MyUserAdmin)