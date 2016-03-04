from __future__ import unicode_literals

import hashlib
from django.db import models

# Create your models here.

class MyUser(models.Model):
	user_id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 100)
	email = models.EmailField(unique = True)
	link_to_dp = models.CharField(max_length = 100)
	type_flag = models.IntegerField(default = 1)
	dob = models.CharField(max_length = 100)
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

