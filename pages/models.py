from django.db import models

class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tour(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория'
    )
    title = models.CharField('Название (Страна: Город)', max_length=150)
    description = models.TextField('Короткое описание')
    price = models.IntegerField('Цена в баллах')
    days = models.IntegerField('Количество дней')
    dates = models.CharField('Даты тура', max_length=100)
    image = models.CharField('Путь к фото в static', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'