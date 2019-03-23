from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='blog-home'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user_posts'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]
