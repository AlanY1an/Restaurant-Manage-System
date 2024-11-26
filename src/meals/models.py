from django.db import models

#URL 友好的格式
from django.utils.text import slugify
# Create your models here.

class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category', on_delete = models.SET_NULL, null = True)
    people = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to='meals/')
    slug = models.SlugField(blank=True, null=True)

    #save中定义：URL 友好的格式
    def save(self, *args, **kwargs):
        # 如果没有定义过 就定义 如果有就跳过避免网址变化
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meals, self).save(*args, **kwargs)

# Meta 类包含模型的元数据，帮助 Django 更好地理解模型的意图，并在管理界面中更友好地显示模型名称。
    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
