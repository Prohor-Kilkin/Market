from django.utils.http import urlencode

from goods.models import Categories
from django import template


register = template.Library()  # регистрируем шаблонный тег


@register.simple_tag()
def tag_categories():
    """Добавляем список категорий на все страницы, где он есть.
     По этому имени мы сможем вызвать функцию в шаблоне, а она вернет из бд
     категории товаров"""
    return Categories.objects.all()


@register.simple_tag(takes_context=True)  # Будут доступны контекстные переменные из views:title,goods,slug_url и параметры из GET запроса.
def change_params(context, **kwargs):
    """Функция возвращает строку, сформированную из полученного словаря,
     которую вставляем в шаблон catalog, в пагинацию."""
    query = context['request'].GET.dict()  # формируем словарь
    query.update(kwargs)  # передаем значение kwargs из шаблона catalog (page=page)
    return urlencode(query)

