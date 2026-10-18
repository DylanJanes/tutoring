from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser,Availability



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
    "email",
    "username",
    "displayName",
    "tutorFor",
    "is_staff",]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("displayName","tutorFor",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":("displayName","tutorFor",)}),)

class AvailabilityAdmin(admin.ModelAdmin):
    list_display=("user","day","start_time","end_time")
    list_filter=("day",)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Availability,AvailabilityAdmin)

# Register your models here.
