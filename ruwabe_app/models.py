# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
	def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True, first_name=None, last_name=None):
		if not email:
			raise ValueError("An Email Address is Mandatory")
		user_obj=self.model(
			email=self.normalize_email(email)
			)
		user_obj.set_password(password)
		user_obj.staff=is_staff
		user_obj.first_name=first_name
		user_obj.last_name=last_name
		user_obj.admin=is_admin
		user_obj.active=is_active
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self, email, password=None, first_name=None, last_name=None):
		user=self.create_user(
			email,
			password=password,
			first_name=first_name,
			last_name=last_name,
			is_staff=True,
			is_admin=True
			)

	def create_superuser(self, email, password=None, first_name=None, last_name=None):
		user=self.create_user(
			email,
			password=password,
			first_name=first_name,
			last_name=last_name,
			is_staff=True,
			is_admin=True
			)

class User(AbstractBaseUser):
	email=models.EmailField(unique=True, max_length=255)
	USERNAME_FIELD='email'
	active=models.BooleanField(default=True)
	staff=models.BooleanField(default=False)
	admin=models.BooleanField(default=False)
	first_name=models.CharField(max_length=150, null=True)
	last_name=models.CharField(max_length=150, null=True)
	timestamp=models.DateTimeField(auto_now_add=True)

	REQUIRED_FIELDS=['first_name', 'last_name']

	objects=UserManager()

	def __str__(self):
		return self.email

	def get_short_name(self):
		return self.email
	def get_full_name(self):
		return self.email

	@property
	def is_staff(self):
		return self.admin
	@property
	def is_admin(self):
		return self.admin
	@property
	def is_active(self):
	    return self.active
	def has_perm(self, perm, obj=None):
		return True#self.admin
	def has_module_perms(self, app_label):
		return True#self.admin

class UserProfile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	id_number=models.CharField(max_length=15, null=False)
	phone_number=models.CharField(max_length=15, null=True)
	location=models.CharField(max_length=150, null=True)
	source=models.URLField(null=True)


class WorkInfo(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	occupation_details=models.CharField(max_length=150, null=True)
	earnings_range_per_month=models.FloatField(max_length=150, null=True)

class Guarantor(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	first_name=models.CharField(max_length=150)
	last_name=models.CharField(max_length=150)
	phone_number=models.CharField(max_length=15)
	relationship=models.CharField(max_length=50)
	workmate=models.CharField(max_length=150)
	occupation=models.CharField(max_length=150)



