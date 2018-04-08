# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  *;

# Register your models here.

class my_users(admin.ModelAdmin):
	search_fields=['email']
	list_display=['__str__', 'id', 'email', 'first_name', 'last_name', 'password']
	class meta:
		model=User

admin.site.register(User, my_users)

admin.site.register(UserProfile)

admin.site.register(WorkInfo)


admin.site.register(Guarantor)