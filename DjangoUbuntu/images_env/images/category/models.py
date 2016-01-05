from django.db import models
from django import forms

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    order = models.IntegerField()

    class Meta:
        db_table = "category"
        ordering = ['-id']
		
		
#form category
class CategoryForm(forms.ModelForm):
   title = forms.CharField(label='Title', min_length=3, max_length=100, strip=True)
   order = forms.IntegerField(label='Order', min_value=1)

   class Meta:
       model = Category
       fields = ['title', 'order']