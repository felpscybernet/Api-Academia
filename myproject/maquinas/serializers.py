from rest_framework import serializers
from maquinas.models import Fabricante

class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:

        model = Fabricante
        fields = '__all__'