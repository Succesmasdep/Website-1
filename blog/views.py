from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'

class ArtikelDetail(DetailView):
    model = Post
    template_name = 'blog/artikel_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_artikel.html"
    # fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "blog/update_artikel.html"
    # fields = ['judul','konten']
