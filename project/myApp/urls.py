from django.urls import re_path
from . import views

app_name='myapp'
urlpatterns = [
    re_path(r'^$', views.hello, name='hello'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/draft/$', views.post_draft_list, name='post_draft_list'),
    re_path(r'^post/search/$', views.full_search, name='post_search_list'),

]
