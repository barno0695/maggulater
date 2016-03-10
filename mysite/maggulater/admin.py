from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Admin)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Test)
admin.site.register(Performance_Sheet)
admin.site.register(Enrolls)
admin.site.register(Notice)