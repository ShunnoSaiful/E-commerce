from django.conf.urls import url
from django.urls import path
from .views import product_search_view

app_name = 'search'
urlpatterns = [
    url(r'^$', product_search_view, name='product_search_view'),
]