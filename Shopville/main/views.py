from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Goods
from .forms import GoodsForm


def catalog(request):
    content = {
        'items': Goods.objects.order_by('id')[:]
    }
    print('--------------------------------------------------------------------------------')
    for item in Goods.objects.order_by('id')[:]:
        print(item.item_image)
        print('___')
    return render(request, 'main/catalog.html', content)


def item(request, item_name):
    context = {
        'item': Goods.objects.get(item_name=item_name)
    }
    return render(request, 'main/item.html', context)


def add_product(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GoodsForm()
    return render(request, 'main/add_product.html', {'form': form})
