from django.shortcuts import render, get_object_or_404

from .models import Post, Video
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.

def all_posts(request):
    post_list = Post.objects.order_by('-write_date')[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, 'forum/show_all_posts.html', context)
    
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'forum/post_detail.html', {'post': post})
    
    #render videos

def video_view(request):
    videos = Video.objects.all()
    return render(request, "forum/videos.html", {"videos": videos})

def search(request):
    
    searched = request.POST.get('searched')
    results = Post.objects.none()
    if searched:
        results = Post.objects.filter(Q(title__contains=searched) | Q(content__contains=searched) | Q(author__contains=searched))
    
    return render(request, "forum/search.html", {"results": results, "searched": searched})