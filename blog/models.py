from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# from ckeditor.fields import RichTechField 


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio =  models.TextField()
    # profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profiles")
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    judul = models.CharField(max_length=255)
    # header_images = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # konten = RichTextField(blank=True, null=True)
    konten = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    kategori = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.judul + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("detail-artikel", kwargs={"pk": self.pk})
    