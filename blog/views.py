from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    cats = Category.objects.all()
    ordering =['-pub_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu  = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    

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

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/hapus_artikel.html"
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    template_name = 'blog/add_category.html'
    fields = '__all__'
    
def CategoryView(request, cats):
    category_posts = Post.objects.filter(kategori=cats.replace('-', ' '))
    return render(request, 'blog/categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts })

def CategoryListView(request):
    cat_menu_list  = Category.objects.all()
    return render(request, 'blog/categories_list.html', {'cat_menu_list':cat_menu_list})
