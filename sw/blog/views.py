from django.shortcuts import render
from .models import Post

def index(request):
	post_list = Post.objects.all()
	return render(request, 'blog/post_list.html', {
		'post_list' : post_list,
	})

# Create your views here.
