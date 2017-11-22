from django import forms
from django.forms.models import BaseInlineFormSet
from .models import ProductBody


class ProductBodyModelForm(forms.ModelForm):

    class Meta:
        model = ProductBody
        fields = ["language", "name"]
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
