from __future__ import unicode_literals
import hashlib
from django.db import models
from datetime import datetime

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
		assert password
		hashed = hashlib.md5(password).hexdigest()
		print self.password, hashed
		return self.password == hashed
	def set_password(self, password):
		self.password = password
	def serialize(self):
		return {
			'user_id' : self.user_id,
			'name' : self.name,
			'email' : self.email,
			'password' : self.password,
			'link_to_dp' : self.link_to_dp,
			'type_flag' : self.type_flag,
			'dob' : self.dob
			# This is an example how to deal with Many2Many relations
			#	'many2many'  : self.serialize_many2many
			}

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
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'course_name' : self.course_name,
			'course_id' : self.course_id,
			'faculty_name' : self.faculty.Faculty_Id.name,
			'faculty_email' : self.faculty.Faculty_Id.email,
			'faculty_dp' : self.faculty.Faculty_Id.link_to_dp,
			'prereq' : self.prereq,
			'syllabus' : self.syllabus,
			'approved' : self.approved
			# This is an example how to deal with Many2Many relations
		#	'many2many'  : self.serialize_many2many
		}
#Lecture
class Lecture(models.Model):
	Lecture_Id = models.AutoField(primary_key = True)
	Course_Id = models.ForeignKey(Course, on_delete =models.CASCADE)
	Notes = models.TextField(default = "")
	Date_Time = models.DateTimeField(default = datetime.now())

	Topic = models.CharField(max_length = 100, default = "Topic Not Mentioned")
	Link = models.CharField(max_length = 100)

	def setDate(self, date):
		self.Date_Time = date
	def setNotes(self , notes):
		self.Notes = notes

	def getDate(self):
		return self.Date_Time.day

	def setLink(self, link):
		self.Link = link
	def serialize(self):

		return {
			'Lecture_Id' : self.Lecture_Id,
			'Course_Id' : self.Course_Id.serialize(),
			'Notes' : self.Notes ,
			'Day' : self.Date_Time.day,
			'Month' : self.Date_Time.month,
			'Year' : self.Date_Time.year,
			'Topic' : self.Topic,
			'Link' : self.Link,
		}
#Test
class Test(models.Model):
	Test_Id = models.AutoField(primary_key = True)
	Lecture_Id = models.ForeignKey(Lecture, on_delete = models.CASCADE)
	Questions = models.TextField(default="")
	Answer_Sheet = models.TextField(default="")
	Questions = models.TextField(default = "")
	Answer_Sheet = models.TextField(default = "")
	totalMarks = models.IntegerField(default = 100)
	def setQuestions(self, Questions):
		self.Questions = Questions

	def setAnswers(self, Answers):
		self.Answer_Sheet = Answers
	def serialize(self):
		return {
			'Test_Id' : self.Test_Id,
			'Lecture_Id' : self.Lecture_Id.serialize(),
			'Questions' : self.Questions,
			'Answer_Sheet' : self.Answer_Sheet,
			'totalMarks' : self.totalMarks,
		}
#Performance
class Performance_Sheet(models.Model):
	Student_Id = models.ForeignKey(Student, on_delete = models.CASCADE)
	Test_Id = models.ForeignKey(Test , on_delete = models.CASCADE)
	Marks_Obtained = models.FloatField(default = 0)
	Marks_Total = models.FloatField(default = 100)
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'Student_Id' : self.Student_Id.Student_Id.user_id,
			'Student_Name' : self.Student_Id.Student_Id.name,
			'Course Name' : self.Test_Id.Lecture_Id.Course_Id.course_name,
			'Topic' : self.Test_Id.Lecture_Id.Topic,
			'Marks_Obtained' : self.Marks_Obtained,
			'Marks_Total' : self.Marks_Total
			# This is an example how to deal with Many2Many relations
		#	'many2many'  : self.serialize_many2many
		}
# Enrolls relationship
class Enrolls(models.Model):
	enrolls_id = models.AutoField(primary_key = True)
	student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
	course_id = models.ForeignKey(Course, on_delete = models.CASCADE)
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'enrolls_id' : self.enrolls_id,
			'student_id' : self.student_id,
			'course_id' : self.course_id
			# This is an example how to deal with Many2Many relations
			#	'many2many'  : self.serialize_many2many
		}
# Notice Table
class Notice(models.Model):
	notice_id = models.AutoField( primary_key = True)
	timestamp = models.DateTimeField(default =datetime.now())
	message = models.CharField(max_length = 500)
	c_id = models.ForeignKey(Course, on_delete = models.CASCADE)
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'notice_id' : self.notice_id,
			'day' : self.timestamp.day,
			'month' : self.timestamp.month,
			'year' : self.timestamp.year,
			'message' : self.message,
			'c_id' : self.c_id.serialize()
			# This is an example how to deal with Many2Many relations
		#	'many2many'  : self.serialize_many2many
		}
