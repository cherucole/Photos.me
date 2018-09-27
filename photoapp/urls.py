from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.images, name='imagesHome'),
    url(r'^search/', views.search_results, name='search_results')

]