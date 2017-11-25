from django import forms
from django.forms.models import BaseInlineFormSet
from ckeditor.widgets import CKEditorWidget
from .models import *


class ProductBodyModelForm(forms.ModelForm):

    class Meta:
        model = ProductBody
        fields = ["language", "name", "title", "description", "keywords"]
        widgets = {
            'language': forms.TextInput(
                attrs={'readonly': 'readonly', 'style': 'border-color:white;'}
            )
        }


class ProductBodyInlineFormSet(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        kwargs['initial'] = [{'language': x[0]} for x in ProductBody.languages]
        self.can_delete = False
        super(ProductBodyInlineFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


class MultiOmegaModelForm(forms.ModelForm):
    popup = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = MultiOmega
        fields = ["language", "product", "popup"]


class MultiVitaminModelForm(forms.ModelForm):
    popup = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = MultiVitamin
        fields = ["language", "product", "popup"]


class VitaminCModelForm(forms.ModelForm):
    popup = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = VitaminC
        fields = ["language", "product", "popup"]


class UkachivanieModelForm(forms.ModelForm):
    popup = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Ukachivanie
        fields = ["language", "product", "popup"]


class JeleykiModelForm(forms.ModelForm):
    popup = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Jeleyki
        fields = ["language", "product", "popup"]


class ShipuchieModelForm(forms.ModelForm):
    popup = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Shipuchie
        fields = ["language", "product", "popup"]


class NaborModelForm(forms.ModelForm):
    popup = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Nabor
        fields = ["language", "product", "popup"]
