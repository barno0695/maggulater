from __future__ import unicode_literals
import hashlib
from django.db import models

# Create your models here.
#User
class MyUser(models.Model):
	user_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100)
	email = models.EmailField(unique = True)
	link_to_dp = models.CharField(max_length = 100)
	type_flag = models.IntegerField(default = 1)
	dob = models.DateField(max_length = 100)
	password = models.CharField(max_length = 100)
	def make_password(self ,password):
		assert password
		hashedpassword = hashlib.md5(password).hexdigest()
		return hashedpassword
	def check_password(self, password):
		hashed = make_password(password)
		return self.password == hashed
	def set_password(self, password):
		self.password = password

#Student
class Student(models.Model):
	Student_Id = models.ForeignKey(MyUser ,on_delete=models.CASCADE, primary_key = True)

#Faculty
class Faculty(models.Model):
    Faculty_Id = models.ForeignKey(MyUser,on_delete=models.CASCADE, primary_key = True)

#Admin
class Admin(models.Model):
	Admin_Id = models.ForeignKey(MyUser, on_delete=models.CASCADE,primary_key = True)

#Course
class Course(models.Model):
    course_id = models.AutoField(primary_key = True)
    faculty = models.ForeignKey(Faculty ,on_delete=models.CASCADE)
    course_name = models.CharField(max_length = 30)
    prereq = models.IntegerField(default = -1)
    syllabus = models.CharField(max_length = 500)
    approved = models.IntegerField(default = 0 ) # 1 after admin approves the course
    def approve(self):
        self.approve = 1

    def setSyllabus(self, syl):
        self.syllabus = syl

#Lecture
class Lecture(models.Model):
    Lecture_Id = models.AutoField(primary_key = True)
    Course_Id = models.ForeignKey(Course, on_delete =models.CASCADE)
    Notes = models.TextField
    Date_Time = models.DateTimeField
    Topic = models.TextField
    Link = models.CharField(max_length = 100)
    # Initialization func
    def __init__ (self, timestamp , topic , course_id):
        self.Date_Time = timestamp
        self.Topic = topic
        self.Course_Id = course_id

    def setNotes(self , notes):
        self.Notes = notes 

    def setLink(self, link):
        self.Link = link 

#Test
class Test(models.Model):
    Test_Id = models.AutoField(primary_key = True)
    Lecture_Id = models.ForeignKey(Lecture, on_delete = models.CASCADE)
    Questions = models.TextField
    Answer_Sheet = models.TextField

#Performance 
class Performance_Sheet(models.Model):
    Student_Id = models.ForeignKey(Student, unique = True , on_delete = models.CASCADE)
    Test_Id = models.ForeignKey(Test ,  unique = True, on_delete = models.CASCADE)
    Marks_Obtained = models.FloatField
    Marks_Total = models.FloatField

# Enrolls relationship
class Enrolls(models.Model):
    enrolls_id = models.AutoField(primary_key = True)
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete = models.CASCADE)

# Notice Table
class Notice(models.Model):
    notice_id = models.IntegerField( primary_key = True)
    timestamp = models.DateTimeField
    message = models.CharField(max_length = 500)
    c_id = models.ForeignKey(Course, on_delete = models.CASCADE)