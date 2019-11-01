from django.shortcuts import render, redirect, HttpResponse
from .models import Invoice, InvoiceProduct
from django.views.generic import ListView
from .forms import invoice_inline_form, InvoiceForm, InvoiceProductForm
from django.db import transaction
from inventory.models import Inventory
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

import pdfkit


options = {
    'page-size': 'Letter',
    'margin-top': '0.5in',
    'margin-right': '0.5in',
    'margin-bottom': '0.5in',
    'margin-left': '0.5in',
    'encoding': "UTF-8",
    'no-outline': None
}




def invoice_pdf_view(request,id):
	invoice_obj = Invoice.objects.get(id=id)
	context = {
	'invoice_obj':invoice_obj
	}
	return render(request, "invoice/invoice_pdf_view.html",context)


def pdf_view(request,id=None):
	projectUrl = request.get_host() + '/invoice/pdf/view/' + id + '/'
	pdf = pdfkit.from_url(projectUrl, False, options=options)
	response = HttpResponse(pdf,content_type='application/pdf')
	response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
	# attachment
	return response



def invoice_view(request,id):
	invoice_obj = Invoice.objects.get(id=id)
	context = {
		'invoice_obj':invoice_obj
	}
	return render(request, "invoice/invoice_view.html", context)

class InvoiceList(LoginRequiredMixin, ListView):
	model = Invoice
	template_name = 'invoice/invoice_list.html'
	context_object_name = 'invoice_list'
	ordering = "-pk"

	def get_context_data(self,**kwargs):
		data = super(InvoiceList,self).get_context_data(**kwargs)
		data["invoice_form"] = InvoiceForm()
		data["invoice_ini_form"] = invoice_inline_form()
		return data

@login_required
def create_invoice(request):
	if request.method == 'POST':
		form1 = InvoiceForm(request.POST)
		form2 = invoice_inline_form(request.POST)
		if form1.is_valid() and form2.is_valid():
			form1.instance.created_by = request.user
			inv_form = form1.save()
			with transaction.atomic():
				form2.instance = inv_form
				form2.save()

			inv_total = 0
			inv_obj = Invoice.objects.get(id=form1.instance.id)
			inv_pro = InvoiceProduct.objects.filter(invoice=inv_obj)

			for product in inv_pro:
				pro_total = product.quantity * product.price
				product.total_price = pro_total
				product.save()
				inv_total = inv_total + pro_total


				inven_obj = Inventory.objects.get(product=product.product)
				inven_obj.stock = inven_obj.stock - product.quantity
				inven_obj.save()

			discount_price = inv_total * inv_obj.discount / 100
			inv_final_price = inv_total - discount_price

			inv_obj.total_invoice_price = inv_final_price
			inv_obj.save()




		return redirect("/invoice/list/")

@login_required
def update_invoice(request,id):
	in_obj = Invoice.objects.get(id=id)
	if request.method == 'POST':
		form1 = InvoiceForm(request.POST, instance=in_obj)
		form2 = invoice_inline_form(request.POST, instance=in_obj)
		if form1.is_valid() and form2.is_valid():
			form1.instance.created_by = request.user
			inv_form = form1.save()
			with transaction.atomic():
				form2.instance = inv_form
				form2.save()

			inv_total = 0
			inv_obj = Invoice.objects.get(id=form1.instance.id)
			inv_pro = InvoiceProduct.objects.filter(invoice=inv_obj)

			for product in inv_pro:
				pro_total = product.quantity * product.price
				product.total_price = pro_total
				product.save()
				inv_total = inv_total + pro_total


			discount_price = inv_total * inv_obj.discount / 100
			inv_final_price = inv_total - discount_price

			inv_obj.total_invoice_price = inv_final_price
			inv_obj.save()


			pros = Product.objects.all()
			for pro in pros:
				inv_pros = InvoiceProduct.objects.filter(product=pro)
				inventory = Inventory.objects.get(product=pro)
				total_stock = inventory.total_stock
				total = 0
				for inv_pr in inv_pros:
					total = total + inv_pr.quantity

				inventory.stock = total_stock - total
				inventory.save()
				total = 0


			return redirect("/invoice/list/")

	else:
		form1 = InvoiceForm(instance=in_obj)
		form2 = invoice_inline_form(instance=in_obj)

		context = {
			'form1':form1,
			'form2':form2,
		}

	return render(request, 'invoice/invoice_update.html', context)
