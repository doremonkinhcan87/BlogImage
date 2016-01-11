# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from datetime import datetime   

class Document(models.Model):
	id = models.AutoField(primary_key=True)
	docfile = models.ImageField(upload_to='image/')
	title = models.CharField(max_length=256, default= '')
	pub_date = models.DateTimeField(auto_now_add=True, blank=True)

class DocumentForm(forms.ModelForm):
	docfile = forms.ImageField(label='Select a file')
	title = forms.CharField(max_length=256, label='Title')
	class Meta:
		model = Document
		fields = ('docfile','title')
