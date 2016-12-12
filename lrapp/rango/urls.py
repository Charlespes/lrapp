from django.conf.urls import url

from . import views

urlpatterns = [
    # specific category
    url(r'^category/(?P<category_slug_name>[\w\-]+)/$', views.category_detail, name='category_detail'),

    # add category
    url(r'^add_category/new/$', views.add_or_update_category, name='add_category'),

    # update category
    url(r'^edit_category/(?P<category_slug_name>[\w\-]+)/$', views.add_or_update_category, name='edit_category'),

    # add page
    url(r'^(?P<category_slug_name>[\w\-]+)/add_page/new/$', views.add_or_update_page, name='add_page'),

    # update page
    url(r'^(?P<category_slug_name>[\w\-]+)/edit_page/(?P<pk>[\d]+)/$', views.add_or_update_page, name='edit_page'),

    # delete page
    url(r'^page/(?P<pk>[\d\-]+)/delete/$', views.page_delete, name='page_delete'),
]
