from rest_framework import serializers
from .models import Motorista

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'
        extra_kwargs = {
            'nome': {'help_text': 'Nome completo do motorista'},
            'email': {'help_text': 'E-mail válido do motorista'},
            'telefone': {'help_text': 'Número de telefone com DDD'},
            'endereco': {'help_text': 'Endereço completo'},
            'veiculo': {'help_text': 'Tipo do veículo (MOTO, CARRO_HATCH, CARRO_SEDAN, CAMINHONETE)'},
        }
