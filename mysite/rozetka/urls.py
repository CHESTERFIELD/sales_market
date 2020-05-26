"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from rozetka import views
from rozetka.views import CategoryProductList, ProductDetail

urlpatterns = [
    path('categories/', views.get_rozetka_category, name='rozetka-category-page'),
    path('<category_slug>/', CategoryProductList.as_view(), name='category-page'),
    path('<str:category_slug>/<str:product_slug>/', ProductDetail.as_view(), name='product-page'),
]


