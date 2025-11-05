from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
    path('posts/<int:pk>/comments/', views.PostCommentListView.as_view(), name='post-comments'),
    path('comments/create/', views.CommentCreateView.as_view(), name='comment-create'),

]
