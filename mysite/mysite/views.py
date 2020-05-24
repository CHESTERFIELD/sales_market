from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView
from django_filters.views import FilterView

from rozetka.filter import ProductFilter
from rozetka.models import Product, Category


def get_rozetka_category(request):
    queryset = Category.objects.all()
    return render(request, 'category_page.html', context={"objects": queryset})


def home(request):
    product_queryset = Product.objects.order_by("-sale")[:20]
    category_queryset = Category.objects.all()
    context = {
        "objects": product_queryset,
        "categories": category_queryset,

    }
    return render(request, 'main_page.html', context=context)


def get_category_page_and_products_on_it(request):

    category = Category.objects.get(name=request.GET.get['category_name'])
    product_list = category.category_product.all()
    # Show 20 contacts per page.
    paginator = Paginator(product_list, 20)

    page_number = request.GET.get('page')
    try:
        # Если существует, то выбираем эту страницу
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # Если None, то выбираем первую страницу
        page_obj = paginator.get_page(1)
    except EmptyPage:
        # Если вышли за последнюю страницу, то возвращаем последнюю
        page_obj = paginator.get_page(paginator.num_pages)

    return render(request, 'list.html', {'page_obj': page_obj})


class CollectionViews(FilterView):
    template_name = 'list.html'
    model = Product
    paginate_by = 20
    filterset_class = ProductFilter
    context_object_name = 'products'

    def get_queryset(self):
        qs = self.model.objects.all()
        if self.kwargs.get('category_name'):
            qs = qs.filter(category__name=self.kwargs['category_name'])
        return qs



