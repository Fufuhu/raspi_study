from django.contrib import admin
from django.urls import path

from viewer.views.list_view import GalleryListView

urlpatterns = [
    path('list/', GalleryListView.as_view(), name='list'),
]