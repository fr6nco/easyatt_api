from rest_framework import serializers
from models import Company, Location


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description')


class LocationSerializer(serializers.ModelSerializer):
    # Used by the update field, write only
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), write_only=True)
    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'company')


class LocationDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'company')


class CompanyDetailSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(read_only=True, many=True)
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'locations')
