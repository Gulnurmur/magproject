from django.shortcuts import render
from .models import *
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy


class ProfileView(CreateView):
    template_name = 'profiles.html'
    models = Profile
    success_url = reverse_lazy('index')

class PostView(CreateView):
    template_name = 'projects.html'
    models = Post
    success_url = reverse_lazy('index')

class BookList(ListView):
    template_name = 'jobs.html'
    models = Book
    success_url = reverse_lazy('index')