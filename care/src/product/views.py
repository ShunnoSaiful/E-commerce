from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from .models import Product
from invoice.models import Invoice
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
# Create your views here.
@login_required
def home(request):
	invoice = Invoice.objects.all().order_by("-pk")
	todays_sell = 0
	todays_invs = invoice.filter(invoice_date = timezone.now().date())
	for inv in todays_invs:
		todays_sell = todays_sell + inv.total_invoice_price
	product = Product.objects.all()
	context = {
		"total_invoice":invoice.count(),
		"recent_invoice":invoice[:5],
		"total_product":product.count(),
		"todays_sell":todays_sell,
	}
	return render(request,'home.html', context)

class ProductList(LoginRequiredMixin, ListView):
	model = Product
	template_name = 'product/product_list.html'
	context_object_name = 'product_list'
	ordering = "-pk"

	def get_context_data(self,**kwargs):
		data = super(ProductList,self).get_context_data(**kwargs)
		data["product_form"] = ProductForm()
		return data

class ProductCreate(LoginRequiredMixin, CreateView):
	model = Product
	template_name = 'product/product_create.html'
	form_class = ProductForm
	success_url = '/product/list/'

class ProductUpdate(LoginRequiredMixin, UpdateView):
	model = Product
	template_name = 'product/product_update.html'
	form_class = ProductForm
	success_url = '/product/list/'
