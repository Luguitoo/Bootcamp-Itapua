
# Create your views here.
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages

def index(request):
    articles = Article.objects.all()
    params = {
        'articles': articles,
    }
    return render(request, 'blog/index.html', params)

def create(request):
    if (request.method == 'POST'): 
        obj = Article()
        article = ArticleForm(request.POST, instance=obj)
        article.save()
        messages.add_message(request, messages.SUCCESS, "Blog Creado!!!")
        return redirect('index') 
    else:
        params = { 
            'form': ArticleForm(),
        }
        return render(request, 'blog/create.html', params)
    
def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    params = {
        'article': article,
    }
    return render(request, 'blog/detail.html', params)

def edit(request, article_id):
    article = Article.objects.get(id=article_id)
    if (request.method == 'POST'):
        article = ArticleForm(request.POST, instance=article)
        article.save()
        article.save()
        return redirect('detail', article_id)
    else:
        form = ArticleForm(initial={
            'title': article.title,
            'content': article.content,
        })
        params = {
            'article': article,
            'form': form,
        }
        return render(request, 'blog/edit.html', params)

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    if (request.method == 'POST'):
        article.delete()
        return redirect('index')
    else:
        params = {
            'article': article,
        }
        return render(request, 'blog/delete.html', params)