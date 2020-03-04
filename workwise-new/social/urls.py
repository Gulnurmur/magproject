from django.urls import path
from .views import *
app_name='social'
urlpatterns = [
    path('profile/',ProfileView.as_view(),name='profile'),
    path('project/',PostView.as_view(),name='project'),
    path('job/',BookList.as_view(),name='job'),
]