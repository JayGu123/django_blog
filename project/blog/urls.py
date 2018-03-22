from django.urls import re_path
from blog.feed import AllowPostsRss
from . import views

app_name = 'myblog'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),
    re_path(r'^archives/(?P<year>\d+)/(?P<month>\d+)/$', views.ArchivesView.as_view(), name='archives'),
    re_path(r'^categories/(?P<pk>\d+)/$', views.CategoryView.as_view(), name='categories'),
    re_path(r'tags/(?P<pk>\d+)/$', views.TagView.as_view(), name='tags'),
    re_path(r'all/rss/$', AllowPostsRss(), name='rss'),
]