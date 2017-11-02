from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_todo, name='add_todo'),
    url(r'^todo/(?P<todo_id>\w{0,50})/$', views.todo, name='todo'),
    url(r'^todo/delete/(?P<todo_id>\w{0,50})/$', views.delete_todo, name='delete_todo'),
    url(r'^todo/edit/(?P<todo_id>\w{0,50})/$', views.edit_todo, name='edit_todo'),
]