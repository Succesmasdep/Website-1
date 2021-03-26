from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Post(models.Model):
    judul = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    konten = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    # kategori = models.CharField(max_length=50)

    def __str__(self):
        return self.judul

    def get_absolute_url(self):
        return reverse("detail-artikel", kwargs={"pk": self.pk})
    