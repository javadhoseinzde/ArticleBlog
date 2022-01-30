from unicodedata import name
from django.urls import path
from .views import ArticleDetail, ArticleList
app_name = "blog"

urlpatterns = [
    path("", ArticleList.as_view(), name="Articles"),
    path("detail/<slug:slug>", ArticleDetail.as_view(), name="detail")
]