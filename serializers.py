from rest_framework import serializers 
from .models import SaltRh_Clientes

class SaltRh_ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaltRh_Clientes
        fields = ('id', 'Nome', 'Sobrenome', 'E-mail Profissional', 'Celular', 'Empresa', 'Número de Colaboradores', 'Cargo')
        fields = '__all__'
