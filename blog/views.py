from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'

class ArtikelDetail(DetailView):
    model = Post
    template_name = 'blog/artikel_detail.html'

class AddPostView(CreateView):
    model = Post
    template_name = "blog/post_artikel.html"
    fields = '__all__'
