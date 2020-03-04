from django import forms
from .models import Profile,Post,Book
from django.contrib.auth.forms import

class ProfileForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': '',
            'pleaceholder':'Your name'
        })
    )
    surname = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'',
            'pleaceholder':'Your surname'
        })
    )
    class Meta:
        model = Profile
        fields = ['name','surname']


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        label='',
        widget=forms.Select(attrs={
            'class':'',
            'placeholder':'select category'
        })
    )

    text = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'',
            'placeholder':'enter text'
        })
    )
    class Meta:
        model = Post
        fields = ['category','text']


class BookForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class':'',
            'pleaceholder':'Title',
        })
    )
    class Meta:
        model = Book
        fields = ['title']
 
    