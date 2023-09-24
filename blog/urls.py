from django.urls import path
from .views import create_blog, read_blog

urlpatterns = [
    path("blog-added/", create_blog, name="blog_added"),
    path("blog-view/", read_blog)
]
