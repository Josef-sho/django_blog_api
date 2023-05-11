from django.urls import path
from .views import ListPostsView, CreatePostView, UpdatePostView, DeletePostView,login_view

urlpatterns = [
    path('posts/', ListPostsView.as_view(), name='list_posts'),
    path('posts/create/', CreatePostView.as_view(), name='create_post'),
    path('posts/<int:pk>/update/', UpdatePostView.as_view(), name='update_post'),
    path('posts/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    path('login/', login_view, name='login'),
]
