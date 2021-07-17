from django.shortcuts import render
from forum.models import Post

def index(request):
    # Get all posts
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts': posts})