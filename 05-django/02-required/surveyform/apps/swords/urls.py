from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wordit/', views.wordit),
    url(r'^$', views.swords),
]