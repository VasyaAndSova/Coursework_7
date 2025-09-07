from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок блога")
    content = models.TextField(blank=True, null=True, verbose_name="Содержимое блога")
    image = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="Превью блога",
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров", help_text="Укажите количество просмотров", default=0
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", "is_published"]

    def __str__(self):
        return self.title
