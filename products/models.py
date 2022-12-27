from django.db import models

class Product(models.Model):
    title = models.CharField(verbose_name='Продукт', max_length=100)
    number = models.IntegerField(verbose_name='Номер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'