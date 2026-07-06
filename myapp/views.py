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
    elif request.method == 'POST':
        data = request.data
        serializers = StudentSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    elif request.method == 'PUT':
        data = request.data
        student_id = Student.objects.get(id=data['id'])
        serializers = StudentSerializers(student_id, data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    elif request.method == 'PATCH':
        data = request.data
        student_id = Student.objects.get(id=data['id'])
        serializers = StudentSerializers(student_id, data=data, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    else:
        data = request.data
        student_id = Student.objects.get(id=data['id'])
        student_id.delete()
        return Response({'massage':'successfull delete student !'})

