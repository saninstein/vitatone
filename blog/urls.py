from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('<slug:slug>', PostDetailView.as_view(), name='post_ru'),
    path('<str:lang>/<slug:slug>', PostDetailView.as_view(), name='post'),
    path('<str:lang>', PostListView.as_view(), name='posts'),
    path('', PostListView.as_view(), name='posts_ru'),
]