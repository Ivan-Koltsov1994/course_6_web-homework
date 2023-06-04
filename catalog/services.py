from django.core.mail import send_mail


def send_deactivate_email(user):
    send_mail(
        'Вас деактивировали'
    )