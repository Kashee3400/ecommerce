
from django import template
from decimal import Decimal
from core.models import CartItem,OrderItem,Order

register = template.Library()

@register.filter(name='discount')
def get_discounted_price(book):
    if book.discount:
        percentage = Decimal(str(book.discount.percentage))
        discounted_price = book.price - (book.price * (percentage / 100))
        return discounted_price.quantize(Decimal('0.01'))
    else:
        return book.price.quantize(Decimal('0.01'))


@register.filter(name='subtotal')
def subtotal(item):
    percentage = Decimal(str(item.book.discount.percentage))
    discounted_price = item.book.price - (item.book.price * (percentage / 100))
    return item.quantity *  discounted_price

@register.filter(name='itemtotal')
def itemtotal(item):
    percentage = Decimal(str(item.book.discount.percentage))
    discounted_price = item.book.price - (item.book.price * (percentage / 100))
    return item.quantity *  discounted_price


@register.simple_tag
def total_cart_price(user):
    cart_item = CartItem.objects.filter(user=user)
    total_price=0
    for item in cart_item:
        total_price += item.quantity * item.book.get_discounted_price()
    return total_price


@register.simple_tag
def total_order_item_price(id):
    order_item = OrderItem.objects.filter(order_id=id)
    total_price=0
    for item in order_item:
        total_price += item.quantity * item.book.get_discounted_price()
    return total_price