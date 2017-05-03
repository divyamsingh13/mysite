from django.db import models
from django import forms
from django.contrib.auth.
# Create your models here.
class BlogPost(models.Model):
	first=models.CharField(max_length=150)
	last=models.CharField(max_length=150)
	email=models.EmailField(max_length=150)
	password=models.CharField(('password'),max_length=150)
	timestamp=models.DateTimeField()
	
class BlogPostForm(forms.ModelForm):
	class Meta:
		model=BlogPost
		exclude=('timestamp',)