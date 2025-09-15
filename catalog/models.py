from django.db import models

from config import settings


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.TextField(blank=True, null=True, verbose_name="Описание продукта")
    image = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=15,
        verbose_name="Цена за покупку",
        blank=True,
        null=True,
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров", help_text="Укажите количество просмотров", default=0
    )

    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец продукта",
        related_name="products",
        null=True,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]
        permissions = [("can_unpublish_product", "Can unpublish product")]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование категории", help_text="Введите наименование категории"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание категории", help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
