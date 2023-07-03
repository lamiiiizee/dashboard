from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'year', 'author', 'cover', 'description', 'price']
        widgets = {
            'cover': forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }