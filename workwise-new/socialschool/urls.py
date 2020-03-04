
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('project/',PostView.as_view(),name='project'),
    path('job/',BookList.as_view(),name='job'),
]
