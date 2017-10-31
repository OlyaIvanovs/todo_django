from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_todo, name='add_todo'),
    url(r'^todo/(?P<todo_id>\w{0,50})/$', views.todo, name='todo'),
]