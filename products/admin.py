from django.contrib import admin
from .forms import *
from .models import *


class ProductBodyInline(admin.StackedInline):
    model = ProductBody
    form = ProductBodyModelForm
    extra = 3
    max_num = 3
    formset = ProductBodyInlineFormSet
    view_on_site = True

    def view_on_site(self, obj):
        return obj.get_absolute_url()


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    readonly_fields = ('image_tag',)
    inlines = [ProductBodyInline]



admin.site.register(Product, ProductAdmin)
