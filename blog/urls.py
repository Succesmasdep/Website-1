from django.urls import path
from .views import HomeView, ArtikelDetail, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArtikelDetail.as_view(), name='detail-artikel'),
    path('add_post/', AddPostView.as_view(), name='post_artikel')
    ]