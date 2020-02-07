from django.conf.urls import url
from django.urls import path
from accounts.views import login_page, register_page

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),
]