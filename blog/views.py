from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import forms

from .models import blog_collection


def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
       
        blog_records = {
        "title": title,
        "description": description,
        }
        blog_collection.insert_one(blog_records)

        return render(request, "blog_post.html")
    
    if request.method == "GET":
        return render(request, "blog_post.html")


def read_blog(request):
    blog_list = blog_collection.find()
    context = {
        "blog_list": blog_list
    }
    return render(request, "blog_list.html", context)
