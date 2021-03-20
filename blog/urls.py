from django.urls import path
from .views import HomeView, ArtikelDetail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArtikelDetail.as_view(), name='detail-artikel'),
    ]