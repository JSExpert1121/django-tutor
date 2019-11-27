from django.urls import path
from .views import (
    create_blog_view,
    blog_detail_view,
    edit_blog_view
)

app_name = 'blog'
urlpatterns = [
    path('create', create_blog_view, name='create'),
    path('<slug>', blog_detail_view, name='detail'),
    path('<slug>/edit', edit_blog_view, name='edit')
]
