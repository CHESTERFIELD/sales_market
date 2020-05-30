from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from rozetka.models import Product, Category
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(
                request,
                username=username,
                password=password
            )
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = RegisterForm()
    args = {'form': form}
    return render(request, 'registration/register.html', args)



def home(request):
    product_queryset = Product.objects.order_by("-sale")[:20]
    category_queryset = Category.objects.all()
    if request.user.is_authenticated:
        favourites = Product.objects.filter(id__in=request.user.bookmarkproduct_set.values_list('obj', flat=True))
    else:
        favourites = []
    context = {
        "objects": product_queryset,
        "categories": category_queryset,
        'favourites': favourites,
    }
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

        return redirect('product-page', category_slug=bookmark.obj.category.slug, product_slug=bookmark.obj.slug)
