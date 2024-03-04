from django.core.paginator import Paginator
from django.shortcuts import render
from goods.models import Products


# Create your views here.


def catalog(request, category_slug):
    """Выводим товары по категориям, если в категории нет товаров,
    то выводится "Ничего нет" """
    page = request.GET.get('page', 1)  # получаем текущую страницу для пагинации из get запроса
    on_sale = request.GET.get('on_sale', None)  # фильтр товаров по акции
    order_by = request.GET.get('order_by', None) # фильтр товаров по цене

    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

        if not goods.exists():
            return render(request, 'goods/index.html', {"content": "Ничего нет"})

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

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
