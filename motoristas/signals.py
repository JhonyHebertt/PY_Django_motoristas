from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Motorista
from .tasks import enviar_email_motorista

@receiver(post_save, sender=Motorista)
def motorista_salvo(sender, instance, created, **kwargs):
    if created:
        assunto = "Motorista cadastrado"
        mensagem = f"Motorista {instance.nome} foi criado com sucesso."
    else:
        assunto = "Motorista atualizado"
        mensagem = f"Motorista {instance.nome} foi atualizado."

    enviar_email_motorista.delay(assunto, mensagem, instance.email)

@receiver(post_delete, sender=Motorista)
def motorista_removido(sender, instance, **kwargs):
    assunto = "Motorista removido"
    mensagem = f"Motorista {instance.nome} foi excluído do sistema."
    enviar_email_motorista.delay(assunto, mensagem, instance.email)
