# coding: utf-8
from django import forms

from .models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.",
                           widget=forms.TextInput(attrs={'placeholder': 'name'}))
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Please enter the title of the page.',
                            widget=forms.TextInput(attrs={'placeholder': 'title'}))
    url = forms.URLField(max_length=200, help_text='Please enter the url of the page.',
                         widget=forms.URLInput(attrs={'placeholder': 'url'}))
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    desc = forms.TextInput()

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs['placeholder'] = 'desc...'

    class Meta:
        model = Page
        exclude = ('category', 'owner')
