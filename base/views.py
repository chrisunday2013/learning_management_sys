from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TeacherSerializer 
from rest_framework import permissions
from rest_framework import generics
from . import models




class TeacherList(generics.ListCreateAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes=[permissions.IsAuthenticated]


class Teacher_update_destroy_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer 
    permission_classes=[permissions.IsAuthenticated]   
