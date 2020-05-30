from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from rozetka.filters import ProductFilter
from rozetka.models import Category, Product


def get_rozetka_category(request):
    queryset = Category.objects.all()
    return render(request, 'category_page.html', context={"objects": queryset})


class CategoryProductList(ListView):
    template_name = 'list.html'
    paginate_by = 21

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        product_list = self.category.category_product.all()
        return product_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category_queryset = Category.objects.all()
        favourites = Product.objects.filter(id__in=self.request.user.bookmarkproduct_set.values_list('obj', flat=True))

        context['category'] = self.category
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        context['categories'] = category_queryset
        context['favourites'] = favourites
        return context


class ProductDetail(DetailView):

    model = Product
    template_name = "product_detail.html"

    def get_object(self, queryset=None):
        product = self.model.objects.get(slug=self.kwargs['product_slug'])
        print(product)
        return product

    def get_context_data(self, **kwargs):
        category_queryset = Category.objects.all()
        if self.request.user.is_authenticated:
            favourites = Product.objects.filter(id__in=self.request.user.bookmarkproduct_set.values_list('obj', flat=True))
        else:
            favourites = []
        context = {
            'object': self.object,
            "categories": category_queryset,
            'favourites': favourites,
        }
        return context