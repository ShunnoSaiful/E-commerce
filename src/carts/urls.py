from django.conf.urls import url
from django.urls import path
from .views import cart_home, cart_update

app_name = 'carts'
urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^update/$', cart_update, name='update'),
]