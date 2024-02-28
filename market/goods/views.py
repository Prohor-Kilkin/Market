from django.core.paginator import Paginator
from django.shortcuts import render
from goods.models import Products


# Create your views here.


def catalog(request, category_slug, page=1):
    """Выводим товары по категориям, если в категории нет товаров,
    то выводится "Ничего нет" """

    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

        if not goods.exists():
            return render(request, 'goods/index.html', {"content": "Ничего нет"})

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        'title': 'Каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    """ Достаем из бд slug каждого товара"""
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context)
