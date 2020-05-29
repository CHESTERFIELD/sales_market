from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from rozetka.models import Product, Category
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        if form.is_valid():
            form.save()
        return redirect("/")

    else:

        form = RegisterForm()
        return render(response, "registration/register.html", {"form": form})


def home(request):
    product_queryset = Product.objects.order_by("-sale")[:20]
    category_queryset = Category.objects.all()
    favourites = Product.objects.filter(id__in=request.user.bookmarkproduct_set.values_list('obj', flat=True))
    context = {
        "objects": product_queryset,
        "categories": category_queryset,
        'favourites': favourites,
    }
    print(context)
    return render(request, 'main_page.html', context=context)


class BookmarkView(View):
    # в данную переменную будет устанавливаться модель закладок, которую необходимо обработать
    model = None

    def post(self, request, pk):
        # нам потребуется пользователь
        user = auth.get_user(request)
        # пытаемся получить закладку из таблицы, или создать новую
        bookmark, created = self.model.objects.get_or_create(user=user, obj_id=pk)
        # если не была создана новая закладка,
        # то считаем, что запрос был на удаление закладки
        if not created:
            bookmark.delete()

        return redirect(home)
