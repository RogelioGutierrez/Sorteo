from celery import shared_task 

from django.core.mail import send_mail

from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    sleep(10)
    send_mail(
    'Subject here',
    'Here is the message.',
        'rogelio.18.91@gmail.com',
        ['rogelio.18.91@gmail.com'],
        fail_silently=False,
    )

    return None