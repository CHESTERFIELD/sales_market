from django.db import models

from mysite.utilites.create_slug_with_russian import slugify


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=200)
    link_to_photo = models.CharField(max_length=200)
    old_price = models.FloatField(default="", blank=True, null=True)
    cheaper_price = models.FloatField(default="", blank=True, null=True)
    sale = models.FloatField(default="", blank=True, null=True)
    sale_promo_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 related_name='category_product', null=True, blank=True)
    about = models.TextField(default="", null=True, blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
