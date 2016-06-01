import sys, os
sys.path.append(r"C:\Users\Sam\Documents\django_2\blog")

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from data_search import find_pol

def home(request):
    return render(request, 'blog/home.html')

def search_posts(request):
    return render(request, 'blog/search_posts.html')

def perform_search_posts_action(request):
    return redirect('view_results', name=(request.POST).get('search_name', ""), state=(request.POST).get('search_state', ""))

def view_results(request, name, state):
    if len(name) < 5:
        return redirect('bad_search', reason="broad")
    good_ids = find_pol(name, state)
    posts = Post.objects.filter(id__in=good_ids).order_by('name')
    if (len(posts) > 0):
        return render(request, 'blog/view_results.html', {'posts': posts})
    else:
        return redirect('bad_search', reason="narrow")

def bad_search(request, reason):
    return render(request, 'blog/bad_search.html', {'reason': reason})

