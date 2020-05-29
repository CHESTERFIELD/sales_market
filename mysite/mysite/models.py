from django.contrib.auth.models import User
from django.db import models

from rozetka.models import Product


class BookmarkProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    obj = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = "Избранный товар"
        verbose_name_plural = "Избранные товары"

    def __str__(self):
        return self.user.username

    def get_bookmark_count(self):
        return self.bookmarkproduct_set.all().count()