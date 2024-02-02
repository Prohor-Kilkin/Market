from django.shortcuts import render
from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': 'О нас',
        'text_on_page': "Самый лучший в мире магазин"
    }
    return render(request, 'main/about.html', context)
