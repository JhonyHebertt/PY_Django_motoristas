from rest_framework import viewsets, permissions
from .models import Motorista
from .serializers import MotoristaSerializer
from .tasks import enviar_email_motorista
from rest_framework.response import Response

class MotoristaViewSet(viewsets.ModelViewSet):
    """
    Operações de CRUD para o modelo Motorista.
    """
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Cria um novo motorista e dispara e-mail de notificação.
        """
        instance = serializer.save()
        enviar_email_motorista.delay(f"Motorista {instance.nome} criado com sucesso.")

    def perform_update(self, serializer):
        """
        Atualiza os dados do motorista e envia notificação.
        """
        instance = serializer.save()
        enviar_email_motorista.delay(f"Motorista {instance.nome} atualizado com sucesso.")

    def perform_destroy(self, instance):
        """
        Remove o motorista e dispara notificação.
        """
        nome = instance.nome
        instance.delete()
        enviar_email_motorista.delay(f"Motorista {nome} removido com sucesso.")
