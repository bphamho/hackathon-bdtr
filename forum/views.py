from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext

from .models import Post, Comment, Video
from django.db.models import Q
from django.http import HttpResponse
from community.models import CommunityDetail

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
    communities = CommunityDetail.objects.all()
    return render(request, 'forum/create_new_post_page.html', {'title': "", 'content': "", "communities": communities, "user": request.user})

@login_required
def create_post(request):
    community_filter = request.POST['filter']
    title = request.POST['title']
    content = request.POST['content']
    user = request.POST['username']
    
    communities = CommunityDetail.objects.all()

    if (len(content) == 0 or len(title) == 0):
        old_content = content if len(content) > 0 else ""
        old_title = title if len(title) > 0 else ""
        return render(request, 'forum/create_new_post_page.html', {'title': old_title, 'content': old_content, 'communities': communities})
    new_post = Post(author=user, write_date=datetime.now(), title=title, content=content)
    new_post.save()

    for community in communities:
        if community_filter == community.name:
            community.posts.add(new_post)
    
    return redirect('/forum/' + str(new_post.id), post_detail(request, new_post.id))

@login_required
def create_comment(request):
    user = request.POST['username']
    comment = request.POST['comment']
    pid = request.POST['id']
    post = get_object_or_404(Post, pk=pid)
    if (len(comment) == 0):
        comments = Comment.objects.filter(post_id=pid)
        return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments})
    new_comment = Comment(commentor=user, write_date=datetime.now(), comment=comment, post=post)
    new_comment.save()
    #comments = Comment.objects.filter(post_id=pid)
    return redirect('/forum/' + pid, post_detail(request, pid))
    
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
