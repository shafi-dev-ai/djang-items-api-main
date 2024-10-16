from rest_framework import serializers
from .models import Items, Location

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('__all__')



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')
