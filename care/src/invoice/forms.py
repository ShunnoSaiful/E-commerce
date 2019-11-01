from django.forms import ModelForm, inlineformset_factory
from .models import InvoiceProduct, Invoice

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        exclude = ['created_by','total_invoice_price']


class InvoiceProductForm(ModelForm):
    class Meta:
        model = InvoiceProduct
        exclude = ['total_price']


invoice_inline_form = inlineformset_factory(Invoice, InvoiceProduct,form=InvoiceProductForm, extra=1)
