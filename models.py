from django.db import models

class SaltRh_Clientes(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=25)
    email_profissional = models.EmailField(default='Nome.sobrenome@empresa.com')
    celular = models.CharField(max_length=15, default='(11) 99999-9999')
    empresa = models.CharField(max_length=30)
    número_de_colaboradores = models.IntegerField(default=500)
    cargo = models.CharField(max_length=20, default='Gerente de RH')

    def __str__(self):
        return self.nome 
