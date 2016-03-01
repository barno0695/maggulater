import json
from flask import Flask, make_response, request, url_for, jsonify, render_template, request, redirect
import MySQLdb
from flask.ext.httpauth import HTTPBasicAuth
import os
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy import create_engine
from sqlalchemy import text
from functools import wraps


db = SQLAlchemy()
#User Model
class User(db.Model):
  __tablename__ = 'db_user'
  user_id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(30))
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(128))
  link_to_dp = db.Column(db.String(1000))
  type_flag = db.Column(db.Integer)
  DOB = db.Column(db.String(1000))

  def __init__(self, name, email, password, link_to_dp, type_flag_, dob):
    self.name = name.title()
    self.email = email.lower()
    self.set_password(password)
    self.link_to_dp = link_to_dp
    self.type_flag = type_flag_
    self.DOB = dob

  def set_password(self, password_):
    self.password = generate_password_hash(password_)

  def check_password(self, password_):
    return check_password_hash(self.password, password_)
# Lecture Model
class Lecture(db.Model):
    __tablename__ = 'db_Lecture'
    Lecture_Id = db.Column(db.Integer, primary_key = True)
    Notes = db.Column(db.Text)
    Date_Time = db.Column(db.DateTime)
    Topic = db.Column(db.Text)
    Test = db.relationship('Test', backref = 'Lecture' , lazy = 'dynamic')

    # Initialization func
    def __init__ (self, lec_id, notes , timestamp , topic):
        self.Lecture_Id = lec_id
        self.Notes = notes
        self.Date_Time = timestamp
        self.Topic = topic
# Test Model
class Test(db.Model):
    __tablename__ = 'db_Test'
    Test_Id = db.Column(db.Integer, primary_key = True)
    Lecture_Id = db.Column(db.Integer, db.ForeignKey(Lecture.Lecture_Id))
    Question_Paper = db.relationship('Question', backref = 'Test' , lazy = 'dynamic')
# Student Model
class Student(db.Model):
  __tablename__ = 'db_Student'
  Student_Id = db.Column(db.Integer , db.ForeignKey(User.user_id), primary_key = True)
  Performance_Sheet = db.relationship('Performance_Sheet' , backref = 'Student' , lazy = 'dynamic')
# Faculty Model
class Faculty(db.Model):
  __tablename__ = 'db_Faculty'
  Faculty_Id = db.Column(db.Integer , db.ForeignKey(User.user_id), primary_key = True)
# Admin Model
class Admin(db.Model):
    __tablename__ = 'db_Admin'
    Admin_Id = db.Column(db.Integer, db.ForeignKey(User.user_id), primary_key = True)
# Question Model
class Question(db.Model):
    __tablename__ = 'db_Questions'
    Question_Id = db.Column(db.Integer, db.ForeignKey(Test.Lecture_Id))
    text = db.Column(db.String(200) , primary_key = True)
    answ = db.Column(db.String(200))
    def __init__ (self , qtext ,qansw):
        self.text = qtext
        self.answ = qansw
#Performance Model
class Performance_Sheet(db.Model):
    __tablename__ = 'db_Performance_Sheet'
    Student_Id = db.Column(db.Integer , db.ForeignKey(Student.Student_Id) , primary_key = True)
    Test_Id = db.Column(db.Integer , db.ForeignKey(Test.Test_Id), primary_key = True)
    Marks_Obtained = db.Column(db.Float)
    Marks_Total = db.Column(db.Float)
# Course Table
class Course(db.Model):
    __tablename__= 'db_course'
    course_id = db.Column(db.Integer, primary_key = True)
    faculty = db.Column(db.Integer, db.ForeignKey(Faculty.Faculty_Id))
    course_name = db.Column(db.String(30))
    prereq = db.Column(db.Integer)
    syllabus = db.Column(db.String(500))
    notices = db.relationship('Notice', backref='Course', lazy='dynamic')
    approved = db.Column(db.Integer) # 1 after admin approves the course

    def __init__(self, fid, cid, cname, pre):
        self.faculty = session['user_id']
        self.course_id = cid
        self.course_name = cname
        self.prereq = pre
        self.approved = 0 # Initially unapproved

    def approve(self):
        self.approve = 1

    def setSyllabus(self, syl):
        self.syllabus = syl

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'course_id' : self.course_id,
           'faculty' : self.faculty,
           'course_name' : self.course_name,
           'prereq' : self.prereq,
           'syllabus' : self.syllabus,
           'approved' : self.approved
           # This is an example how to deal with Many2Many relations
        #    'many2many'  : self.serialize_many2many
       }
    @property
    def serialize_many2many(self):
       """
       Return object's relations in easily serializeable format.
       NB! Calls many2many's serialize property.
       """
       return [ item.serialize for item in self.many2many]


# Enrolls relationship
class Enrolls(db.Model):
    __tablename__= 'db_enrolls'
    enrolls_id = db.Column(db.Integer, primary_key = True)
    student_id = db.Column(db.Integer, db.ForeignKey(Student.Student_Id))
    course_id = db.Column(db.Integer, db.ForeignKey(Course.course_id))

    def __init__(self, sid, cid):
        self.student_id = sid
        self.course_id = cid
# Notice Table
class Notice(db.Model):
    __tablename__= 'db_notice'
    notice_id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    message = db.Column(db.String(500))
    c_id = db.Column(db.Integer, db.ForeignKey(Course.course_id))

    def __init__(self, cid, msg):
        self.message = msg
        self.c_id = cid
