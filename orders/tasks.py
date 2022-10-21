from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = f'Dear {order.first_name},\n\nYou have successfully placed an order.\
                Your order id is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'free-protect@ukr.net',
                          [order.email])
    return mail_sent
