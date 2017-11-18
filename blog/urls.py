from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('<str:lang>/<slug:slug>', PostDetailView.as_view(), name='post'),
    path('<slug:slug>', PostDetailView, name='post_ru'),
    path('', PostListView.as_view(), name='posts')
]