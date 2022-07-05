from rest_framework.viewsets import ModelViewSet
from .models import Cars
from .serializers import CarsSerializers

class CarsViewSet(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializers


