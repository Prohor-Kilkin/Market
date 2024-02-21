from goods.models import Categories
from django import template


register = template.Library()  # регистрируем шаблонный тег


@register.simple_tag()
def tag_categories():
    """Добавляем список категорий на все страницы, где он есть.
     По этому имени мы сможем вызвать функцию в шаблоне, а она вернет из бд
     категории товаров"""
    return Categories.objects.all()

