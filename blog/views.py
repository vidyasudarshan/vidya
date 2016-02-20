from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from .forms import PostForm
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/post_list.html', {'posts': posts})
def post_new(request):
	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
