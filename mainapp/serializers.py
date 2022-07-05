from rest_framework import serializers
from .models import Cars

class CarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'title', 'motor', 'photo', 'date_created', 'author')
