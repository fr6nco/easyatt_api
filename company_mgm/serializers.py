from rest_framework import serializers
from models import Company, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'description')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description')


class LocationDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Location
        fields = ('id', 'name', 'description', 'company')


class CompanyDetailSerializer(serializers.ModelSerializer):
    # locations = serializers.StringRelatedField(many=True, read_only=True)
    locations = LocationSerializer(read_only=True, many=True)
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'locations')