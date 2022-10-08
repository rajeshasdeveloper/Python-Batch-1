from re import search
from rest_framework import serializers
from awesome_api.models import Species, Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'birth_year', 'eye_color', 'species')

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('name', 'classification', 'language')