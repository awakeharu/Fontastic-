import re
from django import forms
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	content= models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.pk])

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering =['-id']

	def get_edit_url(self):
		return reverse('blog:comment_edit', args=[self.post.pk, self.pk])

	def get_delete_url(self):
		return reverse('blog:comment_delete', args=[self.post.pk, self.pk])

class UploadFileModel(models.Model):
	title = models.FileField(null=True)

# Create your models here.
