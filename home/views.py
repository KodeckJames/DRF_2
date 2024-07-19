from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from home.serializers import PeopleSerializer

# Create your views here.

@api_view(['GET', 'POST','PUT'])
def index(request):
    courses = {
        "course_name":"Python",
        "learn": ['flask', 'Django', 'Tornado', 'FastApi'],
        "course_provider":'Scalers'
    }
    if request.method == 'GET':
        print('You hit a GET request')
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print('******')
        print(data)
        print('******')
        print('You hit a POST request')
        return Response(courses)
    elif request.method == 'PUT':
        print('You hit a PUT request')
        return Response(courses)
    
@api_view(['GET','POST'])
def person(request):
    if request.Get:
        objs = person.objects.all()
        serializer = PeopleSerializer(objs, many = True)
        return Response(serializer.data)
    else:
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)