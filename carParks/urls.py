from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'cp', views.carParks, name='carParks'),
    url(r'cptests', views.tests, name='carParks'),
]