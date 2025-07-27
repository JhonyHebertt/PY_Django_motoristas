from django.db import models

class Motorista(models.Model):
    VEICULO_CHOICES = [
        ('MOTO', 'Moto'),
        ('HATCH', 'Carro Hatch'),
        ('SEDAN', 'Carro Sedan'),
        ('CAMINHONETE', 'Caminhonete'),
    ]

    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    veiculo = models.CharField(max_length=20, choices=VEICULO_CHOICES)

    def __str__(self):
        return self.nome
