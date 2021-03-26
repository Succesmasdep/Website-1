from django import forms
from .models import Post, Category

cats = Category.objects.all().values_list('name','name')

choices_list = []

for item in cats:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('judul', 'author','kategori', 'konten')
        widgets = {
            'judul' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.Select(attrs={'class': 'form-control'}),
            'kategori' : forms.Select(choices= choices_list, attrs={'class': 'form-control'}),
            'konten' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('judul', 'konten')
        widgets = {
            'judul' : forms.TextInput(attrs={'class':'form-control'}),
            'konten' : forms.Textarea(attrs={'class':'form-control'}),
        }