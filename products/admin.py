from django.contrib import admin
from .forms import *
from .models import *


class ProductBodyInline(admin.StackedInline):
    model = ProductBody
    form = ProductBodyModelForm
    extra = 3
    max_num = 3
    formset = ProductBodyInlineFormSet


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',)
    readonly_fields = ('image_tag',)
    inlines = [ProductBodyInline]


admin.site.register(Product, ProductAdmin)
