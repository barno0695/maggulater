# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(serialize=False, primary_key=True)),
                ('course_name', models.CharField(max_length=30)),
                ('prereq', models.IntegerField(default=-1)),
                ('syllabus', models.CharField(max_length=500)),
                ('approved', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Enrolls',
            fields=[
                ('enrolls_id', models.AutoField(serialize=False, primary_key=True)),
                ('course_id', models.ForeignKey(to='maggulater.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('Lecture_Id', models.AutoField(serialize=False, primary_key=True)),
                ('Topic', models.CharField(default='Topic Not Mentioned', max_length=100)),
                ('Link', models.CharField(max_length=100)),
                ('Course_Id', models.ForeignKey(to='maggulater.Course')),
            ],
        ),
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('link_to_dp', models.CharField(max_length=100)),
                ('type_flag', models.IntegerField(default=1)),
                ('dob', models.DateField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_id', models.IntegerField(serialize=False, primary_key=True)),
                ('message', models.CharField(max_length=500)),
                ('c_id', models.ForeignKey(to='maggulater.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Performance_Sheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('Test_Id', models.AutoField(serialize=False, primary_key=True)),
                ('Lecture_Id', models.ForeignKey(to='maggulater.Lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('Admin_Id', models.ForeignKey(primary_key=True, serialize=False, to='maggulater.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('Faculty_Id', models.ForeignKey(primary_key=True, serialize=False, to='maggulater.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Student_Id', models.ForeignKey(primary_key=True, serialize=False, to='maggulater.myuser')),
            ],
        ),
        migrations.AddField(
            model_name='performance_sheet',
            name='Test_Id',
            field=models.ForeignKey(to='maggulater.Test', unique=True),
        ),
        migrations.AddField(
            model_name='performance_sheet',
            name='Student_Id',
            field=models.ForeignKey(to='maggulater.Student', unique=True),
        ),
        migrations.AddField(
            model_name='enrolls',
            name='student_id',
            field=models.ForeignKey(to='maggulater.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(to='maggulater.Faculty'),
        ),
    ]
