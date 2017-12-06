from django.contrib import admin
from .forms import *
from .models import *


class PostBodyInline(admin.StackedInline):
    model = PostBody
    form = PostBodyModelForm
    extra = 3
    max_num = 3
    formset = PostBodyInlineFormSet
    view_on_site = True

    def view_on_site(self, obj):
        return obj.get_absolute_url()


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    readonly_fields = ('image_tag',)
    inlines = [PostBodyInline]


admin.site.register(Post, PostAdmin)
admin.site.register(PostLink)
