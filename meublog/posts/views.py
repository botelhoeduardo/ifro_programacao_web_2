from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('created_date')
    return render(request, 'blog.html', {'posts' : posts})
