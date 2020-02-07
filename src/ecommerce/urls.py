"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from accounts.views import home_page, login_page, register_page, home_page, about, blog, cart, category, checkout, confirmation, contact, elements, single_blog, single_product, tracking
from products.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home_view, name="home"),
    url(r'^products/', include("products.urls", namespace = "products")),
    url(r'^search/', include("search.urls", namespace = "search")),
    url(r'^cart/', include("carts.urls", namespace = "cart")),
    url(r'^account/', include("accounts.urls", namespace = "accounts")),
    url(r'^about/$', about),
    url(r'^blog/$', blog),
    url(r'^singleblog/$', single_blog),
    url(r'^category/$', category),
    url(r'^contact/$', contact),
    url(r'^confirmation/$', confirmation),
    url(r'^checkout/$', checkout),
    url(r'^elements/$', elements),
    url(r'^tracking/$', tracking),

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
