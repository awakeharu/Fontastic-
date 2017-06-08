from django import forms
from .models import Comment, Post, Question, Call , Upload

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

class CallForm(forms.ModelForm):
	class Meta:
		model = Call
		fields = [
			'title',
			'contents',
		]

class UploadForm(forms.ModelForm):
	class Meta:
		model = Upload
		fields = ['photo',]
