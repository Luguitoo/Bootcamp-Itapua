from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView,  DeleteView
from django.urls import reverse_lazy, reverse
   
class ArticleList(ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = 'articles' 

class ArticleCreate(CreateView):
    model = Article
    template_name = 'blog/create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('index')


class ArticleDetail(DetailView):
    model = Article
    template_name = "blog/detail.html"
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

class ArticleUpdate(UpdateView):
    model = Article
    fields = '__all__'
    template_name = 'blog/edit.html'
    pk_url_kwarg = 'article_id'
    def get_success_url(self):
        return reverse('detail', kwargs={'article_id': self.object.pk})


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'article_id'
