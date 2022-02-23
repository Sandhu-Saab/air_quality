from django.contrib import admin
from . models import contect
# Register your models here.



@admin.register(contect)
class User1Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
