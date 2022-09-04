from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TeacherSerializer 
from . import models 




class TeacherList(APIView):
    def get(self, request):
        teachers=models.Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
