from django.conf.urls import url, include
from django.urls import path
from django.views.generic.base import RedirectView
from .views import index, about

app_name = "frontend"

urlpatterns = [
    path('', index, name='index'),
    path('about/',about,name='about'),


]