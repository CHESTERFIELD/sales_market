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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from mysite import views
from mysite.models import BookmarkProduct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('rozetka/', include('rozetka.urls')),
    path('search/', include('search.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    url('(?P<pk>\d+)/favourites/$', login_required(views.BookmarkView.as_view(model=BookmarkProduct)), name='product_bookmark'),
]


