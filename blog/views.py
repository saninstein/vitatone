from django.views.generic import ListView, DetailView
from .models import Post, PostBody
from products.models import ProductBody


class PostListView(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = PostBody
    template_names = (
        ('ru', "post/index.html"),
        ('en', "post/index_en.html"),
        ('uk', "post/index_uk.html")
    )
    context_object_name = "post_body"
    query_pk_and_slug = True

    def get_template_names(self):
        lang = self.kwargs.get('lang', 'ru')
        return [name[1] for name in self.template_names if name[0] == lang]

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        lang = self.object.language
        exclude_id = self.object.post.id
        foreign_posts = PostBody.objects.filter(post_id=exclude_id)
        context['link'] = { x.language: x.get_absolute_url()  for x in foreign_posts}
        context['posts'] = PostBody.objects.filter(language=lang).exclude(post_id=exclude_id)[:3]
        context['products'] = ProductBody.objects.filter(language=lang)[:3]


        return context
