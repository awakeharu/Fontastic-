from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment ,Question , Call , Upload
from .forms import CommentForm, PostForm , CallForm, QuestionForm , UploadForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse



def index(request):
	post_list = Post.objects.all()
	question_list = Question.objects.all()
	call_list = Call.objects.all()
	return render(request, 'blog/post_list.html', {
		'post_list' : post_list,
		'question_list':question_list,
		'call_list':call_list,

	})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {
			'post' : post,
		})

def question_detail(request, pk):
	question = get_object_or_404(Question, pk=pk)
	return render(request, 'blog/question_detail.html', {
			'question' : question,
		})

def call_detail(request, pk):
	call = get_object_or_404(Call, pk=pk)
	return render(request, 'blog/call_detail.html', {
			'call' : call,
		})

def upload_detail(request, pk):
	request = get_object_or_404(Request, pk=pk)
	return render(request, 'blog/upload_detail.html', {
			'upload' : upload,
		})

@login_required
def post_new(request):
	if request.method=="POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('blog:post_detail' , form.pk)
	else:
		form = PostForm()
	return render(request, "blog/post_form.html",{
		"form":form,
		})
	

@login_required
def comment_new(request, post_pk):
	post = get_object_or_404(Post, pk = post_pk)

	if request.method =='POST':
		form = CommentForm(request.POST, request.FILES)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()
			return redirect('blog:post_detail', post.pk)
	else:
		form = CommentForm()
	return render(request, 'blog/comment_form.html', {
			'form':form,
		})

@login_required
def comment_edit(request, post_pk, pk):
	comment = get_object_or_404(Comment, pk=pk)
	if comment.author != request.user:
		return redirect(comment.post)

	if request.method =='POST':
		form = CommentForm(request.POST, request.FILES, instance=comment)
		if form.is_valid():
			comment = form.save()
			return redirect(comment.post)
	else:
		form = CommentForm(instance=comment)
	return render(request, 'blog/comment_form.html', {
			'form':form,
		})

@login_required
def comment_delete(request, post_pk, pk):
	comment = get_object_or_404(Comment, pk=pk)
	if comment.author != request.user:
		return redirect(comment.post)

	if request.method =='POST':
		comment.delete()
		return redirect(comment.post)

	return render(request, 'blog/comment_confirm_delete.html', {
			'comment': comment,
	})

@login_required
def question_new(request):
	if request.method=="POST":
		form = QuestionForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('blog:question_detail' , form.pk)
	else:
		form = QuestionForm()
	return render(request, "blog/question_form.html",{
		"form":form,
		})

@login_required
def call_new(request):
	if request.method=="POST":
		form = CallForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('blog:call_detail' , form.pk)
	else:
		form = CallForm()
	return render(request, "blog/call_form.html",{
		"form":form,
		})

@login_required
def upload_new(request):
	if request.method=="POST":
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit=False)
			form.save()
			return redirect('blog:upload_detail', form.pk)
	else:
		form = UploadForm()
	return render(request, "blog/upload_form.html",{"form":form})

#파일 업로드

# Create your views here.
