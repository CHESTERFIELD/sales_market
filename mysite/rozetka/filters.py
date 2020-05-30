import django_filters

CHOICES = [
    ["name", "По алфавиту"],
    ["cheaper_price", "Дешевые сверху"],
    ["-cheaper_price", "Дорогие сверху"],
    ["-sale", "Найбольшая скидка"],
    ["sale", "Найменьшая скидка"],
]


class ProductFilter(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(choices=CHOICES, required=True, empty_label="Выберете тип", )


ProductFilter.base_filters['ordering'].label = 'Сортировать как'
