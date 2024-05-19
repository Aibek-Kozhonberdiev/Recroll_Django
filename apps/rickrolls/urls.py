from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_url_rickroll, name='index'),
]
