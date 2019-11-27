from django.urls import path
from .views import (
    create_blog_view
)

app_name = 'blog'
urlpatterns = [
    path('create', create_blog_view, name='create'),
]
