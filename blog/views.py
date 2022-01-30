from django.shortcuts import render, get_object_or_404
from .models import Article
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ArticleList(ListView):
    queryset = Article.objects.all()
    template_name = "blog/article.html"
    context_object_name = "articles"

class ArticleDetail(DetailView):
    template_name = "blog/detail.html"
    context_object_name = "articl"
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Article.objects.filter(slug=slug))