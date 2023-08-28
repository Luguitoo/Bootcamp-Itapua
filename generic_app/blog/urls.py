from django.urls import path
from . import views


urlpatterns = [
    path('', views.ArticleList.as_view(), name='index'),
    path('create', views.ArticleCreate.as_view(), name='create'),
    path('detail/<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
    path('edit/<int:article_id>/', views.ArticleUpdate.as_view(), name='edit'),
    path('delete/<int:article_id>/', views.ArticleDelete.as_view(), name='delete'),
]
