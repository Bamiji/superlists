from django.conf.urls import include, url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(\d+)/$', 'lists.views.view_list', name='view_list'),  
    url(r'^users/(.+)/$', views.my_lists, name='my_lists'),
]
