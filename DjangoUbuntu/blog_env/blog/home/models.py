# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from datetime import datetime   

class Users(models.Model):
	id = models.AutoField(primary_key=True)
	firt_name = models.CharField(max_length=256)
	last_name = models.CharField(max_length=256)
	password = models.CharField(max_length=256)
	role = models.CharField(max_length=256)
	email = models.CharField(max_length=256, default="")
	class Meta:
		db_table = "users"
		ordering = ['-id']
	def __str__(self):
		return self.role
		
		
class UsersForm(forms.ModelForm):
	firt_name = forms.CharField(label='Firt Name', max_length=100, strip=True)
	last_name = forms.CharField(label='Last Name', max_length=100, strip=True)
	password = forms.CharField(label='Password', max_length=100, strip=True)
	role = forms.CharField(label='Role', max_length=100, strip=True)
	email = forms.CharField(label='Email', max_length=100, strip=True)
	class Meta:
		model = Users
		fields = ['firt_name', 'last_name', 'password', 'role', 'email']

class Document(models.Model):
	id = models.AutoField(primary_key=True)
	users = models.ForeignKey(to=Users, related_name="users_id", null=True, blank=True)
	docfile = models.ImageField(upload_to='image/')
	title = models.CharField(max_length=256, default= '')
	pub_date = models.DateTimeField(auto_now_add=True, blank=True)
	class Meta:
		db_table = "document"
		ordering = ['-id']

class DocumentForm(forms.ModelForm):
	users = models.ForeignKey(Users)
	docfile = forms.ImageField(label='Select a file')
	title = forms.CharField(max_length=256, label='Title')
	class Meta:
		model = Document
		fields = ('docfile','title', 'users')

