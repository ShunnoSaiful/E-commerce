from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from .models import Inventory
from .forms import InventoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class InventoryList(LoginRequiredMixin, ListView):
	model = Inventory
	template_name = 'inventory/inventory_list.html'
	context_object_name = 'inventory_list'
	ordering = "-pk"

	def get_context_data(self,**kwargs):
		data = super(InventoryList,self).get_context_data(**kwargs)
		data["inventory_form"] = InventoryForm()
		return data

class InventoryCreate(LoginRequiredMixin, CreateView):
	model = Inventory
	template_name = 'inventory/inventory_create.html'
	form_class = InventoryForm
	success_url = '/inventory/list/'

class InventoryUpdate(LoginRequiredMixin, UpdateView):
	model = Inventory
	template_name = 'inventory/inventory_update.html'
	form_class = InventoryForm
	success_url = '/inventory/list/'
