from django.contrib import admin
from .models import students

admin.site.register(students)

class studentsAdmin(admin.ModelAdmin):
    list_display=('Id','Name','Age','Email','Phone','Address')
    

