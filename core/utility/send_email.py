from nitincom import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from datetime import datetime
from core.models import OrderItem,Logo

def send_order_placed_email(user,order):
    total_price=0
    order_items = OrderItem.objects.filter(order=order)
    for item in order_items:
        total_price += item.quantity * item.book.get_discounted_price()
    context = {'order': order,'total_price':total_price,'logo':Logo.objects.all().first()}
    
    emp_email_html_message = render_to_string('email_template.html', context)
    emp_email = EmailMessage(
        f"Order Placed #{order.order_id}",
        emp_email_html_message,
        settings.EMAIL_HOST_USER,
        [user.email], 
    )
    emp_email.content_subtype = 'html'
    emp_email.send()
    
    
def send_test_mail(user):
    emp_email = EmailMessage(
        f"Order Placed",
        "Order Placed",
        settings.EMAIL_HOST_USER,
        [user.email], 
    )
    emp_email.send()