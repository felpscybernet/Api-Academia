from rest_framework import viewsets
from maquinas.models import Fabricante
from maquinas.serializers import FabricanteSerializer

class FabricanteViewSet(viewsets.ModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer