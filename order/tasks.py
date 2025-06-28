from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_confirmation_email(user_email, order_id):
    subject = "Order Confirmation"
    message = f"Thank you for your order #{order_id}!"
    from_email = "no-reply@example.com"
    
    send_mail(subject, message, from_email, [user_email])
