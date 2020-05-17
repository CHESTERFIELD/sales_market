from django.shortcuts import render

from rozetka.models import Product


def home(request):
    queryset = Product.objects.order_by("-sale")[:32]
    return render(request, 'base.html', context={"objects": queryset})

def most_sale(request):
    # queryset = Product.objetcs.max(sale)[:32]
    return render(request, )