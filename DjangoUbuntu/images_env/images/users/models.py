from django.db import models
from django import forms

# Create your models here.
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
		
		
#form user
class UsersForm(forms.ModelForm):
	firt_name = forms.CharField(label='Firt Name', max_length=100, strip=True)
	last_name = forms.CharField(label='Last Name', max_length=100, strip=True)
	password = forms.CharField(label='Password', max_length=100, strip=True)
	role = forms.CharField(label='Role', max_length=100, strip=True)
	email = forms.CharField(label='Email', max_length=100, strip=True)
	class Meta:
		model = Users
		fields = ['firt_name', 'last_name', 'password', 'role', 'email']
