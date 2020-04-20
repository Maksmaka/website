from django.urls import path
from blogapi import views

urlpatterns = [
    path('blogs/', views.ArticleView.as_view()),
    # path('blogs/<int:pk>/', views.blog_detail),
]
