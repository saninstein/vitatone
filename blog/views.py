from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Post, PostBody
from products.views import MultilangMixin


class PostListView(MultilangMixin, ListView):
    model = PostBody

    template_names = (
        ('ru', "posts/index.html"),
        ('en', "posts/index_en.html"),
        ('uk', "posts/index_uk.html")
    )

    context_object_name = "posts"
    paginate_by = 2

    def get_queryset(self):
        lang = self.kwargs.get('lang', 'ru')
        self.search = self.request.GET.get('search', '')
        if self.search:
            self.paginate_by = None
        return self.model.objects.filter(language=lang, name__icontains=self.search)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["search"] = self.search
        return context


class PostDetailView(MultilangMixin, DetailView):
    model = PostBody
    template_names = (
        ('ru', "post/index.html"),
        ('en', "post/index_en.html"),
        ('uk', "post/index_uk.html")
    )
    context_object_name = "post_body"
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        lang = self.object.language
        exclude_id = self.object.post.id
        foreign_posts = PostBody.objects.filter(post_id=exclude_id)
        context['link'] = { x.language: x.get_absolute_url()  for x in foreign_posts}
        context['posts'] = [x._post.postbody_set.get(language=lang) for x in self.object.post.posts.all()[:3]]

        context['products'] = [x.productbody_set.get(language=lang) for x in self.object.post.products.all()[:3]]
        return context
