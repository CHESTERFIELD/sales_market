import django_filters
from .models import Product

CHOICES = [
    ["name", "По алфавиту"],
    ["cheaper_price", "Дешевые сверху"],
    ["-cheaper_price", "Дорогие сверху"]
]


class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    # cheaper_price__gt = django_filters.NumberFilter(name='cheaper_price', lookup_expr='gt')
    # cheaper_price__lt = django_filters.NumberFilter(name='cheaper_price', lookup_expr='lt')
    ordering = django_filters.OrderingFilter(choices=CHOICES, required=True, empty_label="Выберете тип", field_name="Jopa")

    # class Meta:
    #     model = Product
        # fields = ['name', 'cheaper_price']
        # exclude = [   'slug', ]
        # order_by_field = 'name'