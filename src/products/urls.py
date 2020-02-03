from django.conf.urls import url
from django.urls import path
from .views import product_list_view, product_detail_view

app_name = 'products'
urlpatterns = [
    url(r'^$', product_list_view, name='product_list_view'),
    url(r'^(?P<slug>[\w-]+)/$', product_detail_view, name='detail'),
]