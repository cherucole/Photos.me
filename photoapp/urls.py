from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
url(r'^$', views.show_categories, name='imagesHomeCategory'),
    # url(r'^$', views.images, name='imagesHome'),

    url(r'^search/', views.search_results, name='search_results'),
    url(r'^category/', views.image_category, name='category_results')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)