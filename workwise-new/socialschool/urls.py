
from django.contrib import admin
from django.urls import path, include
# from social.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('social.urls',namespace='social'))
    # path('profile/',ProfileView.as_view(),name='profile'),
    # path('project/',PostView.as_view(),name='project'),
    # path('job/',BookList.as_view(),name='job'),
]
