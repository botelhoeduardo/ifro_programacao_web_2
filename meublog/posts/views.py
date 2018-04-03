from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all().order_by('created_date')
    return render(request, 'blog.html', {'posts' : posts})

def post_novo(request):
    form = PostForm()
    return render(request, 'novo.html', {'form' : form})