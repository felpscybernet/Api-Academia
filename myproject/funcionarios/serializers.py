from rest_framework import serializers
from funcionarios.models import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:

        model = Funcionario
        fields = '__all__'