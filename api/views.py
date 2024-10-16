from rest_framework import generics
from .models import Items , Location
from .serializers import  ItemSerializer, LocationSerializer

# Create your views here.

'''Item Crud'''
class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()

    def get_queryset(self):
        location = self.request.query_params.get('location')
        if location is not None:
            queryset =  queryset.filter(item_location=location)
            return queryset

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()


''' Location Crud'''
class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()