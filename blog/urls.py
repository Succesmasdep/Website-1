from django.urls import path
from .views import HomeView, ArtikelDetail, AddPostView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArtikelDetail.as_view(), name='detail-artikel'),
    path('add_post/', AddPostView.as_view(), name='post-artikel'),
    path('artikel/edit/<int:pk>', PostUpdateView.as_view(), name='edit-artikel'),
    path('artikel/<int:pk>/remove', PostDeleteView.as_view(), name='hapus-artikel'),
    ]