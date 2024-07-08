from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post
# Create your views here.
def home(request):

    meal_list = Meals.objects.all()
    categories= Category.objects.all()
    posts = Post.objects.all()


    context = {
        'meal_list':meal_list,
        'categories': categories,
        'posts':posts,
    }

    return render(request, 'home/index.html', context)


