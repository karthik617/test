from django.db import models

# Create your models here
class Student(models.Model):
	Gender=[
 		('M','male'),
 		('F','Female')
	]
	Student_name=models.CharField(max_length=100)
	Student_roll_no=models.CharField(max_length=3)
	Student_gender=models.CharField(choices=Gender,max_length=1)
	Student_add=models.TextField()
	Student_std=models.ManyToManyField('Standar')
	Student_dob=models.DateField()

class Standar(models.Model):
	std=models.CharField(max_length=100)



	def __str__(self):
		return self.std