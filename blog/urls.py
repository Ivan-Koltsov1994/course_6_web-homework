from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, toggle_publish

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', PostListView.as_view(), name='post_list'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post_item'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/update/<str:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('posts/delete/<str:slug>/', PostDetailView.as_view(), name='post_delete'),
    path('posts/toggle/<str:slug>/', toggle_publish, name='toggle_publish')

]