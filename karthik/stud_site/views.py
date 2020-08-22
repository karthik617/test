from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def home(request):
	students=Student.objects.all()
	return render(request,'home.html',{'students':students})


def student_det(request,stu_id):
	student=Student.objects.get(id=stu_id)
	return render(request,'student.html',{'student':student})