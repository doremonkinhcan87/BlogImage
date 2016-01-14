# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from datetime import datetime   
from django.forms.models import ModelForm

class Users(models.Model):
	id = models.AutoField(primary_key=True)
	firt_name = models.CharField(max_length=256)
	last_name = models.CharField(max_length=256)
	password = models.CharField(max_length=256)
	role = models.CharField(max_length=256)
	email = models.CharField(max_length=256, default="")
	class Meta:
		db_table = "blog_users"
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
		
class Tags(models.Model):
	id = models.AutoField(primary_key=True)
	users = models.ForeignKey(to=Users, related_name="+", null=True, blank=True)
	name = models.CharField(max_length=256)
	class Meta:
		db_table = 'blog_tags'
		ordering = ['-id']
	def __str__(self):
		return self.name
		
class TagsForm(forms.ModelForm):
	name = forms.CharField(label='Name')
	users = models.ForeignKey(Users)
	class Meta:
		model = Tags
		fields = ['users', 'name']

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	users = models.ForeignKey(to=Users, related_name="+", null=True, blank=True)
	name = models.CharField(max_length=256)
	description = models.CharField(max_length=256)
	class Meta:
		db_table = 'blog_category'
		ordering = ['-id']
	def __str__(self):
		return self.name
		
class CategoryForm(forms.ModelForm):
	name = forms.CharField(label='Name')
	users = models.ForeignKey(Users)
	description = forms.CharField(label='Description')
	class Meta:
		model = Tags
		fields = ['users', 'name', 'description']
		
class Document(models.Model):
	id = models.AutoField(primary_key=True)
	users = models.ForeignKey(to=Users, related_name="users_id", null=True, blank=True)
	docfile = models.ImageField(upload_to='image/')
	title = models.CharField(max_length=256, default= '')
	pub_date = models.DateTimeField(auto_now_add=True, blank=True)
	tags = models.ManyToManyField(Tags, related_name="tags_ids")
	category = models.ForeignKey(to=Category, related_name="category_id", null=True, blank=True)
	subtitle = models.CharField(max_length=256, default= '')
	summary = models.TextField(default= '')
	content = models.TextField(default= '')
	publish = models.BooleanField(default=True)
	class Meta:
		db_table = "blog_document"
		ordering = ['-id']

class DocumentForm(forms.ModelForm):
	users = models.ForeignKey(Users)
	tags = models.ManyToManyField(Tags)
	docfile = forms.ImageField(label='Select a file')
	title = forms.CharField(label='Title')
	category = models.ForeignKey(Category)
	subtitle = forms.CharField(label='Subtitle')
	summary = forms.CharField(widget = forms.Textarea)
	content = forms.CharField(widget = forms.Textarea)
	publish = forms.BooleanField()
	class Meta:
		model = Document
		fields = ['docfile','title', 'users', 'tags', 'category', 'subtitle', 'summary', 'content', 'publish']
		widgets = {
			'body': forms.Textarea(),
			'tags': forms.CheckboxSelectMultiple()
			}


