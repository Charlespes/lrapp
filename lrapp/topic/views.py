from django.shortcuts import render
from django.views.generic.list import ListView

from lrapp.rango.models import Category, Page
from lrapp.account.decorators import add_fav_to_dict


@add_fav_to_dict
def index(request, **kwargs):
    category_list = Category.objects.order_by('-likes')[:8]
    page_list = Page.objects.order_by('-likes')[:8]
    kwargs['categories'] = category_list
    kwargs['pages'] = page_list
    return render(request, 'topic/index.html', kwargs)


def about(request):
    return render(request, 'topic/about.html')


def get_category_list(max_results=0, starts_with=''):
    category_list = []
    if starts_with:
        category_list = Category.objects.filter(name__istartswith=starts_with)
    if category_list and max_results > 0:
        if category_list.count > max_results:
            category_list = category_list[:max_results]
    return category_list


def suggest_category(request):
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    category_list = get_category_list(8, starts_with)
    return render(request, 'cats.html', {'categories': category_list})


class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'topic/all_categories.html'
    paginate_by = 3

    def get_queryset(self):
        try:
            a = self.request.GET.get('category',)
        except KeyError:
            a = None

        if a:
            category_list = Category.objects.filter(name__icontains=a)
        else:
            category_list = Category.objects.all()

        return category_list


class PageList(ListView):
    model = Page
    paginate_by = 3
    template_name = 'topic/all_pages.html'
    context_object_name = 'pages'

    def get_queryset(self):
        try:
            a = self.request.GET.get('page_title',)
        except KeyError:
            a = None
        if a:
            page_list = Page.objects.filter(title__icontains=a)
        else:
            page_list = Page.objects.all()
        return page_list

