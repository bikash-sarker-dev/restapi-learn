from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serialisers import StudentSerializers
from . models import Student


# Create your views here.
@api_view(['GET'])
def index(request):
    user = {
        "user":"bikash sarker",
        "age": 23
    }
    return Response(user)


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student(request):
    if request.method == 'GET':
        data = Student.objects.all()
        serializers = StudentSerializers(data, many=True)
        return Response(serializers.data)
        
