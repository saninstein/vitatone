from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('<str:lang>', PostListView.as_view(), name='posts'),
    path('article/<slug:slug>/', PostDetailView.as_view(), name='post_ru'),
    path('article/<str:lang>/<slug:slug>', PostDetailView.as_view(), name='post'),
    path('', PostListView.as_view(), name='posts_ru'),
]