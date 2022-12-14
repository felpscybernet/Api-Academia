from rest_framework import viewsets
from funcionarios.models import Funcionario
from funcionarios.serializers import FuncionarioSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer