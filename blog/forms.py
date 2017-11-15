from django import forms
from django.forms.models import BaseInlineFormSet
from .models import PostBody


class PostBodyModelForm(forms.ModelForm):
    class Meta:
        model = PostBody
        fields = ["language", "title", "text"]
        widgets = {
            'language': forms.TextInput(
                attrs={'readonly': 'readonly', 'style': 'border-color:white;'}
            )
        }


class PostBodyInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        kwargs['initial'] = [
            {'language': 'RU'}, {'language': 'UA'}, {'language': 'EN'}
        ]
        super(PostBodyInlineFormSet, self).__init__(*args, **kwargs)
