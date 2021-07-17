from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from .models import Post, Comment, Video
from django.db.models import Q
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def all_posts(request):
    post_list = Post.objects.order_by('-write_date')[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, 'forum/show_all_posts.html', context)

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments})
    
@login_required
def create_new_post_page(request):
    return render(request, 'forum/create_new_post_page.html')

@login_required
def create_post(request):
  #  if (request.method == 'POST'):
    #    post_form = PostForm(request.POST)
     #   if (post_form.is_valid()):
        #    q = post_form.save()
        #    new_post = Post.objects.filter(id = q.id)
         #   return render(request, 'forum/post_detail.html', {'post': new_post, 'comments': comments})
    title = request.POST['title']
    content = request.POST['content']
    user = request.POST['username']
    new_post = Post(author=user, write_date=datetime.now(), title=title, content=content)
    new_post.save()
    comments = Comment.objects.filter(post_id=new_post)
    return render(request, 'forum/post_detail.html', {'post': new_post, 'comments': comments})

@login_required
def create_comment(request):
    user = request.POST['username']
    comment = request.POST['comment']
    pid = request.POST['id']
    if (len(comment) == 0):
        post = get_object_or_404(Post, pk=pid)
        comments = Comment.objects.filter(post_id=pid)
        return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments})
    post = get_object_or_404(Post, pk=pid)
    new_comment = Comment(commentor=user, write_date=datetime.now(), comment=comment, post=post)
    new_comment.save()
    comments = Comment.objects.filter(post_id=pid)
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments})
    
#render videos
@login_required
def video_view(request):
    videos = Video.objects.all()
    return render(request, "forum/videos.html", {"videos": videos})

@login_required
def search(request):
    
    searched = request.POST.get('searched')
    results = Post.objects.none()
    if searched:
        results = Post.objects.filter(Q(title__contains=searched) | Q(content__contains=searched) | Q(author__contains=searched))
    
    return render(request, "forum/search.html", {"results": results, "searched": searched})
