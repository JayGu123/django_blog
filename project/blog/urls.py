from django.urls import re_path
from . import views

app_name = 'myblog'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),
    re_path(r'^archives/(?P<year>\d+)/(?P<month>\d+)/$', views.ArchivesView.as_view(), name='archives'),
    re_path(r'^categories/(?P<pk>\d+)/$', views.CategoryView.as_view(), name='categories'),
]