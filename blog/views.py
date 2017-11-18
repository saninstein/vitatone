from django.views.generic import ListView, DetailView
from .models import Post, PostBody


class PostListView(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = PostBody
    template_name = "post/index.html"
    context_object_name = "post_body"
    query_pk_and_slug = True

