from django.conf.urls import url

from . import views

urlpatterns = [
    # user homepage
    url(r'^(?P<pk>[\d\-]+)/homepage/$', views.homepage, name='homepage'),

    # add fav category
    url(r'^add_or_remove_fav_category/(?P<category_slug_name>[\w\-]+)/$', views.add_or_remove_fav_category,
        name='add_or_remove_fav_category'),

    # add fav page
    url(r'^add_or_remove_fav_page/(?P<pk>[\d]+)/$', views.add_or_remove_fav_page, name='add_or_remove_fav_page'),
]

