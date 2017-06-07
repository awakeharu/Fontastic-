from django import forms
from .models import Comment, Post, Question, Request

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['message']

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'title',
			'content',
		]

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = [
			'title',
			'contents',
		]

class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = [
			'title',
			'contents',
		]
