from rest_framework import serializers
from .models import Person

# Write your classes here:
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
