from django.db import models

# Create your models here.
class AboutUS(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    image = models.ImageField(upload_to = 'about_us/')

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
        
    def __str__(self) -> str:
        return self.title


class Why_Choose_Us(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()

    class Meta:
        verbose_name = 'Why Choose Us'
        verbose_name_plural = 'Why Choose Us'

    def __str__(self) -> str:
        return self.title

class Chef(models.Model):
    name = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='chef/')
    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chef' 
    
    def __str__(self) -> str:
        return self.name
    
