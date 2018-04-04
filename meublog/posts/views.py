from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all().order_by('created_date')
    return render(request, 'blog.html', {'posts' : posts})

def post_novo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'novo.html', {'form' : form})