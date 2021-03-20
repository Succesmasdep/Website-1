from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('judul', 'author', 'konten')
        widget = {
            'judul' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.Select(attrs={'class':'form-control'}),
            'konten' : forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('judul', 'konten')
        widget = {
            'judul' : forms.TextInput(attrs={'class':'form-control'}),
            'konten' : forms.Textarea(attrs={'class':'form-control'}),
        }