from django.contrib import admin
from .models import Student,Standar
# Register your models here.
@admin.register(Student)
class Student_details(admin.ModelAdmin):
	list_dis=['Student_name','Student_roll_no','Student_gender','Student_add','Student_dob']

@admin.register(Standar)
class Standar_details(admin.ModelAdmin):
	list_dis=['std']
