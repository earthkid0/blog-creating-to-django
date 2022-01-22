from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post
from do_it_Django import settings
import os
# Create your views here.

def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts':recent_posts,
        }
    )

def about_me(request):
    return render(
        request,
        ('single_pages/about_me.html')
    )

def robots(request):
    return render(
        request,
        ('single_pages/robots.txt')

    )
    