from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sumbitted', views.submitted, name="submitted"),
    url(r'^homework1', views.hw1, name="hw1"),
    url(r'^homework2', views.hw2, name="hw2"),
    url(r'^homework3', views.hw3, name="hw3"),
    url(r'^homework4', views.hw4, name="hw4"),
    url(r'^homework5', views.hw5, name="hw5"),
    url(r'^homework6', views.hw6, name="hw6"),
    url(r'^homework7', views.hw7, name="hw7"),
    url(r'^homework8', views.hw8, name="hw8"),
    url(r'^homework9', views.hw9, name="hw9"),
    url(r'^homework10', views.hw10, name="hw10"),
    url(r'^homework11', views.hw11, name="hw11"),
    url(r'^homework12', views.hw12, name="hw12"),
    url(r'^homework13', views.hw13, name="hw13"),
    url(r'^homework14', views.hw14, name="hw14"),
    url(r'^homework15', views.hw15, name="hw15"),
    url(r'^homework16', views.hw16, name="hw16"),
]
