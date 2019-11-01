from django.forms import ModelForm, inlineformset_factory, TextInput
from .models import Inventory


class InventoryForm(ModelForm):
	class Meta:
		model = Inventory
		fields = '__all__'