# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from lrapp.account.decorators import add_fav_to_dict
from .models import Category, Page
from .forms import CategoryForm, PageForm


@add_fav_to_dict
def category_detail(request, category_slug_name, **kwargs):
    try:
        category = Category.objects.get(slug=category_slug_name)
        kwargs['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        kwargs['pages'] = pages
        kwargs['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', kwargs)


@login_required()
def add_or_update_category(request, category_slug_name=None):
    pages = []
    edit = False
    if category_slug_name:
        edit = True
        category = get_object_or_404(Category, slug=category_slug_name)
        if category:
            if category.owner != request.user:
                return HttpResponseForbidden()
            else:
                pages = Page.objects.filter(category=category, owner=request.user)
    else:
        category = Category(owner=request.user)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save(commit=True)
            if pages:
                for page in pages:
                    page.category = category
                    page.save()
            return redirect('rango:category_detail', category_slug_name=category.slug)
        else:
            print form.errors
    else:
        form = CategoryForm(instance=category)
    return render(request, 'rango/add_or_edit_category.html', {'form': form, 'category': category,
                                                               'edit': edit})


@login_required()
def add_or_update_page(request, category_slug_name, pk=None):
    category = get_object_or_404(Category, slug=category_slug_name)
    edit = False
    if pk:
        edit = True
        page = get_object_or_404(Page, pk=pk)
        if page.owner != request.user:
            return HttpResponseForbidden()
    else:
        page = Page(owner=request.user, category=category)
    if request.POST:
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save(commit=True)
            return redirect('rango:category_detail', page.category.slug)
        else:
            print form.errors
    else:
        form = PageForm(instance=page)
    return render(request, 'rango/add_or_edit_page.html', {'form': form, 'page': page, 'category': category,
                                                           'edit': edit})


@login_required()
def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk)
    category_slug_name = page.category.slug
    print category_slug_name
    if page.owner != request.user:
        return HttpResponseForbidden()
    if request.POST:
        page.delete()
        return redirect('rango:category_detail', category_slug_name)
    return render(request, 'rango/page_delete.html', {'page': page, 'category_name': page.category.name})
