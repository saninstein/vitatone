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


class MultiOmegaAdmin(admin.ModelAdmin):
    form = MultiOmegaModelForm

    def view_on_site(self, obj):
        return obj.get_absolute_url()


class MultiVitaminAdmin(admin.ModelAdmin):
    form = MultiVitaminModelForm

    def view_on_site(self, obj):
        return obj.get_absolute_url()


class MultiVitaminAdmin(admin.ModelAdmin):
    form = MultiVitaminModelForm

    def view_on_site(self, obj):
        return obj.get_absolute_url()


class VitaminCAdmin(admin.ModelAdmin):
    form = VitaminCModelForm

    def view_on_site(self, obj):
        return obj.get_absolute_url()


class UkachivanieAdmin(admin.ModelAdmin):
    form = UkachivanieModelForm

    def view_on_site(self, obj):
        return obj.get_absolute_url()


class JeleykiAdmin(admin.ModelAdmin):
    form = JeleykiModelForm

    def view_on_site(self, obj):
        return obj.get_absolute_url()


class ShipuchieAdmin(admin.ModelAdmin):
    form = ShipuchieModelForm

    def view_on_site(self, obj):
        return obj.get_absolute_url()


class NaborAdmin(admin.ModelAdmin):
    form = NaborModelForm

    def view_on_site(self, obj):
        return obj.get_absolute_url()


admin.site.register(Product, ProductAdmin)
admin.site.register(MultiOmega, MultiOmegaAdmin)
admin.site.register(MultiVitamin, MultiVitaminAdmin)
admin.site.register(VitaminC, MultiVitaminAdmin)
admin.site.register(Ukachivanie, UkachivanieAdmin)
admin.site.register(Jeleyki, JeleykiAdmin)
admin.site.register(Shipuchie, ShipuchieAdmin)
admin.site.register(Nabor, NaborAdmin)

