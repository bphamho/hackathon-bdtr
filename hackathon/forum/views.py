from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from .models import Post, Comment

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
# Create your views here.

def all_posts(request):
    post_list = Post.objects.order_by('-write_date')[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, 'forum/show_all_posts.html', context)
    
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments})
    
@login_required
def create_new_post_page(request):
    return render(request, 'forum/create_new_post_page.html')

#NEED TO EDIT THIS FOR THE AUTHOR
@login_required
def create_post(request):
    title = request.POST['title']
    content = request.POST['content']
    print(request.POST)
    user = request.POST['username']
    new_post = Post(author=user, write_date=datetime.now(), title=title, content=content)
    new_post.save()
    comments = Comment.objects.filter(post_id=new_post.id)
    return render(request, 'forum/post_detail.html', {'post': new_post, 'comments': comments})

def comment_page(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'forum/comment_box.html', {'post': post})

