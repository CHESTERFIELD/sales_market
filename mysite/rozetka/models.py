from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    link_to_photo = models.CharField(max_length=200)
    old_price = models.FloatField(default="", blank=True, null=True)
    cheaper_price = models.FloatField(default="", blank=True, null=True)
    sale = models.FloatField(default="", blank=True, null=True)
    sale_promo_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
