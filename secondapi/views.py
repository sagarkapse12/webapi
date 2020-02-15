from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Student
from .serializer import Studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
class Allstudent(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

    def post(self,request,format=None):
        serial=Studentserializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
            return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

class Allstudent1(APIView):
    def get(self,request,student_id,format=None):
        student1=Student.objects.get(pk=int(student_id))
        serial1=Studentserializer(student1)
        return Response(serial1.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,student_id):
        student2=Student.objects.get(pk=int(student_id))
        student2.delete()
        return Response(status=status.HTTP_200_OK)
    def put(self,request,student_id):
        obj=get_object_or_404(Student.objects.all(),pk=int(student_id))
        serial=Studentserializer(data=request.data)
        if serial.is_valid():
            obj=serial.save()
            return Response({'SUCCESS':"STUDENT '{}' UPDATE SUCCESSFULLY".format(obj.fname,obj.lname,obj.add,obj.contact)})
