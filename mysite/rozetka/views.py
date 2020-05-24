from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from rozetka.models import Category


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
        context['category'] = self.category.name
        return context