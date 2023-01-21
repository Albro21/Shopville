from django.shortcuts import render
from .models import Goods
from django.http import HttpResponse


def catalog(request):
    content = {
        'items': Goods.objects.order_by('id')[:]
    }
    return render(request, 'main/catalog.html', content)


def item(request, item_name):
    context = {
        'item': Goods.objects.get(item_name=item_name)
    }
    return render(request, 'main/item.html', context)
