from django.db import models


class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    img = models.ImageField(verbose_name="Фото", upload_to='product/images/', null=True, blank=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

class ListHeader(models.Model):
    value = models.CharField(verbose_name="", max_length=255)
    product = models.ForeignKey(
        Product, verbose_name="Продукт", on_delete=models.CASCADE, related_name="headers")

    def __str__(self):
        return self.value

class ListParagraph(models.Model):
    value = models.TextField(verbose_name='Текст')
    header = models.ForeignKey(
        ListHeader, verbose_name='Заголовок', on_delete=models.CASCADE, related_name='paragraphs')

    def __str__(self):
        return self.value
