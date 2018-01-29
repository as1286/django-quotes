from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="dashboard"),
    url(r'^add$', views.add, name="add_book"),
    url(r'^create$', views.create, name="create_book"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show_book"),
]