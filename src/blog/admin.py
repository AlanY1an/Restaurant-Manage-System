from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin,admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['title','author','category','created']
    serach_fields = ['title','content']
    list_filter = ('category','tags')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)