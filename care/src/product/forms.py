from django.forms import ModelForm, inlineformset_factory, TextInput
from .models import Product


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'