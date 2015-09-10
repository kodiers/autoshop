# encoding=utf-8
# © Quantum Ltd.
# version 1.0.0

# Custom template tags

from django import template

from shop.models import Contacts, Clients, Basket, Pages

register = template.Library()

@register.filter()
def get_verb_action(action):
    """
    For admin panel convert action to verbs
    """
    if action.is_deletion():
        return "удалено"
    elif action.is_addition():
        return "добавлено"
    elif action.is_change():
        return "изменено"

@register.simple_tag()
def get_verbose_field_name(instance, field_name):
    """
    Returns verbose_name for a field.
    """
    return instance._meta.get_field(field_name).verbose_name.title()


@register.inclusion_tag('footer.html')
def show_contacts():
    """
    Show contacts info in footer
    :return: contacts dictionary
    """
    contacts = Contacts.objects.get(pk=1)
    return ({'contacts': contacts })


@register.filter()
def show_basket_count(login=None):
    """
    Show items count in basket
    :param login: username if user is logged
    :return: number of positions in basket
    """
    count = 0
    if login is not None:
        try:
            client = Clients.objects.get(login__username=login)
            baskets = Basket.objects.filter(client=client)
            for basket in baskets:
                count += basket.quantity
        except:
            pass
    return count

@register.filter()
def show_basket_total(login=None):
    """
    Show basket totatl price
    :param login: username if user is logged
    :return: total price for goods in basket
    """
    total = 0
    if login is not None:
        try:
            client = Clients.objects.get(login__username=login)
            baskets = Basket.objects.filter(client=client)
            for basket in baskets:
                total += basket.total_price
        except:
            pass
    return total


@register.inclusion_tag('page_module.html')
def show_pages():
    """

    :return:
    """
    pages = Pages.objects.all().order_by('-modified_date')[:3]
    return ({'pages': pages})


@register.simple_tag()
def show_phone_number():
    """

    :return:
    """
    contacts = Contacts.objects.get(pk=1)
    return contacts.phone
