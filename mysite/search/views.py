from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView

from rozetka.models import Product


class SearchResultsView(ListView):
    model = Product
    template_name = 'search/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        page = self.request.GET.get('page')
        if query:
            object_list = Product.objects.filter(name__icontains=query)
            paginator = Paginator(object_list, 9)

            try:
                # Если существует, то выбираем эту страницу
                object_list = paginator.get_page(page)
            except PageNotAnInteger:
                # Если None, то выбираем первую страницу
                object_list = paginator.get_page(1)
            except EmptyPage:
                # Если вышли за последнюю страницу, то возвращаем последнюю
                object_list = paginator.get_page(paginator.num_pages)
        else:
            object_list = Product.objects.all()

        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context