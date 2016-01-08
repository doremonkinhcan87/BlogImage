# -*- coding: utf-8 -*-
from django.db import models
from django import forms
from datetime import datetime   

class Document(models.Model):
	id = models.AutoField(primary_key=True)
	docfile = models.FileField(upload_to='')
	title = models.CharField(max_length=256, default= '')
	pub_date = models.DateTimeField(blank=True, default=datetime.now)

class DocumentForm(forms.Form):
	docfile = forms.FileField(label='Select a file')
	title = forms.CharField(max_length=256, label='Title')