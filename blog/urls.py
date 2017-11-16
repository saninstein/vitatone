from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    # path('<slug:postslug>'),
    path('', PostListView.as_view(), name='posts')
]