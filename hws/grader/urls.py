from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sumbitted', views.submitted, name="submitted"),
    url(r'^homework1', views.hw1, name="hw1"),
    url(r'^homework2', views.hw2, name="hw2"),
    url(r'^homework4', views.hw4, name="hw4"),
]

