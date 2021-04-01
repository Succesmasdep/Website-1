from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    judul = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    konten = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    kategori = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.judul + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("detail-artikel", kwargs={"pk": self.pk})
    