from django import forms
from .models import Comment,UploadFileModel

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['message']

class UploadFileForm(forms.ModelForm):
	class Meat:
		model = UploadFileModel
		fields = ('title','file')

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['file'].required = False