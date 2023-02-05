from django.forms import ModelForm, Textarea, TextInput, CharField
from .models import Goods


class GoodsForm(ModelForm):
    item_name = CharField(empty_value='', widget=TextInput(attrs={'placeholder': 'Product name'}))
    item_description =  CharField(empty_value='', widget=Textarea(attrs={'placeholder': 'Description'}))

    class Meta:
        model = Goods
        fields = ['item_image', 'item_name', 'item_description', 'price', 'sellers_email']
