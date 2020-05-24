import django_filters
from .models import Product

CHOICES = [
    ["name", "по алфавиту"],
    ["cheaper_price", "дешевые сверху"],
    ["-cheaper_price", "дорогие сверху"]
]


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    cheaper_price__gt = django_filters.NumberFilter(name='cheaper_price', lookup_expr='gt')
    cheaper_price__lt = django_filters.NumberFilter(name='cheaper_price', lookup_expr='lt')
    ordering = django_filters.OrderingFilter(choices=CHOICES, required=True, empty_label=None, )

    class Meta:
        model = Product
        exclude = [field.name for field in Product._meta.fields]
        order_by_field = 'name'