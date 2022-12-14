from rest_framework import viewsets
from Alunos.models import Aluno
from Alunos.serializers import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer