from django.db import models
from django.utils import timezone   
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now())
    category = models.ForeignKey('Category', null = True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='blog/')
    tags = TaggableManager(blank=True)
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    

    def __str__(self):
        return self.title
    
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.category_name

class Comment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, default='Anonymous')
    phone = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return str(self.content)  
    