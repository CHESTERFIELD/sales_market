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
        context['category'] = self.category
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        print(context['filter'])
        return context


class ProductDetail(DetailView):

    model = Product
    template_name = "product_detail.html"

    def get_object(self, queryset=None):
        product = self.model.objects.get(slug=self.kwargs['product_slug'])
        return product

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context