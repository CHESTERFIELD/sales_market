from django.shortcuts import render
from rozetka.models import Product, Category


def home(request):
    product_queryset = Product.objects.order_by("-sale")[:20]
    category_queryset = Category.objects.all()
    context = {
        "objects": product_queryset,
        "categories": category_queryset,

    }
    return render(request, 'main_page.html', context=context)
