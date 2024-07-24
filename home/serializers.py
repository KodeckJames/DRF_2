from rest_framework import serializers
from .models import Person, Color

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name', 'id']


class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1

    def get_color_info(self, obj):
        color_obj = Color.objects.get(id = obj.color.id)
        return {'color_name': color_obj.color_name, 'hex_code': '#000'}

    def validate(self, data):
        special_chars = "!@#$%^&*()-=+?_=,<>/"
        if any(c in special_chars for c in data['name']):
            raise serializers.ValidationError('Name cannot contain special chars')
        # if data.get('age') and data['age'] < 18:
        #     raise serializers.validationError('Age should be grater than 18')
        return data