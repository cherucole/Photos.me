from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[


    url(r'^$', views.show_categories, name='imagesHomeCategory'),
    url(r'^$', views.my_locations, name='location_results'),

    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/', views.my_locations, name='location_results')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)