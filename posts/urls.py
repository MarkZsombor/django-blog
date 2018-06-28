from django.urls import re_path
from posts.views import *

urlpatterns = [
    re_path(r'^$', post_list, name='post_list'),
    re_path(r'^create/$', post_create, name='post_create'),
    re_path(r'^detail/$', post_detail, name='post_detail'),
    re_path(r'^update/$', post_update, name='post_update'),
    re_path(r'^delete/$', post_delete, name='post_delete'),
]
