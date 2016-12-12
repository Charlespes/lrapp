from django.conf.urls import url

from .import views

urlpatterns = [
    # index page
    url(r'^$', views.index, name='index'),

    # about page
    url(r'^about/$', views.about, name='about'),

    # search category
    url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),

    # all categories
    url(r'^all_categories/$', views.CategoryList.as_view(), name='all_categories'),

    # all pages
    url(r'^all_pages/$', views.PageList.as_view(), name='all_pages'),
]
