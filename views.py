from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import SaltRh_Clientes
from .serializers import SaltRh_ClientesSerializer

from rest_framework.permissions import IsAuthenticated

class SaltRh_ClientesViewSet(viewsets.ModelViewSet):
    permissions_class = (IsAuthenticated,)

    queryset = SaltRh_Clientes.objects.all()
    serializer_class = SaltRh_ClientesSerializer
