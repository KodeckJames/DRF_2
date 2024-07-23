from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        depth = 1

    def validate(self, data):
        special_chars = "!@#$%^&*()-=+?_=,<>/"
        if any(c in special_chars for c in data['name']):
            raise serializers.ValidationError('Name cannot contain special chars')
        if data['age'] < 18:
            raise serializers.validationError('Age should be grater than 18')
        return data