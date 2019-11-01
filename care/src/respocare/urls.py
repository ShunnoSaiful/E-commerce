"""respocare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from product.views import home,ProductList,ProductCreate,ProductUpdate
from invoice.views import InvoiceList, create_invoice, update_invoice, invoice_view, invoice_pdf_view, pdf_view
from inventory.views import InventoryList,InventoryCreate,InventoryUpdate



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^invoice/view/(?P<id>[\d]+)/$', invoice_view, name='invoice_view'),
    url(r'^invoice/pdf/view/(?P<id>[\d]+)/$', invoice_pdf_view, name='invoice_pdf_view'),
    url(r'^invoice/pdf/download/(?P<id>[\d]+)/$', pdf_view, name='pdf_view'),
    url(r'^product/list/$', ProductList.as_view(), name="product_list"),
    url(r'^product/create/$', ProductCreate.as_view(), name="product_create"),
    url(r'^product/update/(?P<pk>[\d]+)/$', ProductUpdate.as_view(), name="product_update"),
    url(r'^invoice/list/$', InvoiceList.as_view(), name="invoice_list"),
    url(r'^invoice/create/$', create_invoice, name="invoice_create"),
    url(r'^inventory/list/$', InventoryList.as_view(), name="inventory_list"),
    url(r'^inventory/create/$', InventoryCreate.as_view(), name="inventory_create"),
    url(r'^inventory/update/(?P<pk>[\d]+)/$', InventoryUpdate.as_view(), name="inventory_update"),
    url(r'^invoice/update/(?P<id>[\d]+)/$', update_invoice, name="update_invoice"),
    url(r'^accounts/', include("accounts.urls")),

]


admin.site.site_header = "RESPO CARE ADMIN"
admin.site.site_title = "RESPO CARE"
