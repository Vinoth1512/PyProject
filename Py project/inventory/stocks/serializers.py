from rest_framework import serializers
from stocks.models import *


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'
        
class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class LocationLookupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['id','location_name']

class CompanyDetailSerializer(serializers.ModelSerializer):
    location_id = LocationLookupSerializer()

    class Meta:
        model = Company
        fields = '__all__'