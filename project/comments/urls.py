from django.urls import re_path
from . import views

app_name = 'mycomment'
urlpatterns = [
    re_path(r'^comment/post/(?P<post_pk>\d+)/$', views.post_comment, name='post_comment'),
]