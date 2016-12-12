from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from lrapp.rango.models import Category, Page
from .models import FavCategory, FavPage
from lrapp.account.decorators import add_fav_to_dict


@add_fav_to_dict
def homepage(request, pk, **kwargs):
    user = get_object_or_404(User, pk=pk)
    category_list = Category.objects.filter(favcategory__user=user)
    page_list = Page.objects.filter(favpage__user=user)
    created_categories = Category.objects.filter(owner=user)
    created_pages = Page.objects.filter(owner=user)
    kwargs.update({'categories': category_list, 'pages': page_list, 'name': user,
                   'created_categories': created_categories,
                   'created_pages': created_pages})
    return render(request, 'account/homepage.html', kwargs)


@login_required()
def add_or_remove_fav_category(request, category_slug_name):
    category = get_object_or_404(Category, slug=category_slug_name)
    fc = get_object_or_404(FavCategory, user=request.user)
    likes = category.likes
    if category in fc.categories.all():
        fc.categories.remove(category)
        category.likes = likes - 1
        category.save()
    else:
        fc.categories.add(category)
        category.likes = likes + 1
        category.save()
    the_page = request.GET.get('the_page')
    if the_page == 'index':
        return redirect('topic:index')
    elif the_page == "category_detail":
        return redirect('rango:category_detail', category_slug_name)
    elif the_page == "homepage":
        return redirect('account:homepage', category.owner.pk)


@login_required()
def add_or_remove_fav_page(request, pk):
    page = get_object_or_404(Page, pk=pk)
    category = page.category
    fp = get_object_or_404(FavPage, user=request.user)
    likes = page.likes
    if page in fp.pages.all():
        fp.pages.remove(page)
        page.likes = likes - 1
        page.save()
    else:
        fp.pages.add(page)
        page.likes = likes + 1
        page.save()
    the_page = request.GET.get('the_page')
    if the_page == 'index':
        return redirect('topic:index')
    elif the_page == 'category_detail':
        return redirect('rango:category_detail', category.slug)
    elif the_page == 'homepage':
        return redirect('account:homepage', page.owner.pk)
