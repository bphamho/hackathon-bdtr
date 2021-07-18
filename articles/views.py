from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from datetime import datetime
# Create your views here.
def create_new_article_page(request):
    return render(request, 'create_new_article_page.html')

def create_article(request):
    author = request.POST['username']
    title = request.POST['title']
    content = request.POST['content']
    if (len(content) == 0 or len(title) == 0):
        old_content = content if len(content) > 0 else ""
        old_title = title if len(title) > 0 else ""
        return render(request, 'articles/create_new_article_page.html', {'title': old_title, 'content': old_content})
    new_article = Article(author=author, write_date=datetime.now(), title=title, content=content)
    new_article.save()
    return redirect('/articles/' + str(new_article.id), article_detail(request, new_article.id))

@login_required
def all_articles(request):
    article_list = Article.objects.order_by('-write_date')[:5]
    context = {
        'articles': article_list,
    }
    return render(request, 'articles.html', context)

@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})