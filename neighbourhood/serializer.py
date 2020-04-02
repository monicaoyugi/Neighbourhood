from rest_framework import serializers
from .models import Neighbourhood, Business, Profile, Posts

class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = ('neighbourhood_name', 'location', 'number_of_amenities', 'number_of_estates')

