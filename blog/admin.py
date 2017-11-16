from django.contrib import admin
from .forms import *
from .models import *


class PostBodyInline(admin.StackedInline):
    model = PostBody
    form = PostBodyModelForm
    extra = 3
    max_num = 3
    formset = PostBodyInlineFormSet


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    readonly_fields = ('image_tag',)
    inlines = [PostBodyInline]


admin.site.register(Post, PostAdmin)
