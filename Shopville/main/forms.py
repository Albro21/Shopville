from django.forms import ModelForm
from .models import Goods


class GoodsForm(ModelForm):
    class Meta:
        model = Goods
        fields = ['item_image', 'item_name', 'item_description', 'price', 'sellers_email']
