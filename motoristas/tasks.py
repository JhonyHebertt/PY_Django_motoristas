from celery import shared_task
from django.core.mail import send_mail

@shared_task
def enviar_email_motorista(assunto, mensagem, destinatario):
    send_mail(
        subject=assunto,
        message=mensagem,
        from_email=None,  # usa DEFAULT_FROM_EMAIL
        recipient_list=[destinatario],
        fail_silently=False,
    )
