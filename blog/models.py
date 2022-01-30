from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
	title = models.CharField(max_length=100, unique=True,null=True)
	slug = models.SlugField(max_length=100, unique=True, null=True)
	active = models.BooleanField(default=True)
	position = models.IntegerField()

	def __str__(self):
		return self.title


class Article(models.Model):
	STATUS = (
		("d", "پیش نویس"),
		("p", "منتشر شده"),
	)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=100)
	slug = models.CharField(max_length=100, unique=True, null=True)
	category = models.ForeignKey(Category, null=True,on_delete=models.SET_NULL)
	pic = models.ImageField(upload_to="images/")
	description = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=1, choices=STATUS, default="d")

	def __str__(self):
		return self.title

"""class Comment(models.Model):
	pass
"""
