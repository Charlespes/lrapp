from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^categories/$', views.CategoryList.as_view(), name='category-list'),
    url(r'^categories/(?P<pk>[\d]+)/$', views.CategoryDetail.as_view(), name='category-detail'),
    url(r'^pages/$', views.PageList.as_view(), name='page-list'),
    url(r'^pages/(?P<pk>[\d]+)/$', views.PageDetail.as_view(), name='page-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[\d]+)/$', views.UserDetail, name='user-detail'),
]
