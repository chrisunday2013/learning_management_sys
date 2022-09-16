from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CategorySerializer, ChapterSerializer, CourseSerializer, TeacherSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework import generics
from . import models




class TeacherList(generics.ListCreateAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated]


class Teacher_update_destroy_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer 
    # permission_classes=[permissions.IsAuthenticated]   


@csrf_exempt
def teacher_login(request):
    email=request.POST['email']
    password=request.POST['password']

    teacherData=models.Teacher.objects.get(email=email,password=password)
    if teacherData:
         return JsonResponse({'bool':True, 'teacher_id':teacherData.id})
    else:
        return JsonResponse({'bool':False})    



class CategoryList(generics.ListCreateAPIView):
    queryset=models.CourseCategory.objects.all()
    serializer_class=CategorySerializer
    # permission_classes=[permissions.IsAuthenticated]



class CourseList(generics.ListCreateAPIView):
    queryset=models.Course.objects.all()
    serializer_class=CourseSerializer
    # permission_classes=[permissions.IsAuthenticated]



class TeacherCourseList(generics.ListCreateAPIView):
    serializer_class=CourseSerializer

    def get_queryset(self):
        teacher_id=self.kwargs['teacher_id']
        teacher=models.Teacher.objects.get(pk=teacher_id)
        return models.Course.objects.filter(teacher=teacher)



class TeacherCourse_upate_detail_delete(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Course.objects.all()
    serializer_class=CourseSerializer     




class ChapterList(generics.ListCreateAPIView):
    queryset=models.Chapter.objects.all()
    serializer_class=ChapterSerializer



class CourseChapterList(generics.ListAPIView):
    serializer_class=ChapterSerializer
    
    def get_queryset(self):
        course_id=self.kwargs['course_id']
        course=models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)




class Chapter_upate_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Chapter.objects.all()
    serializer_class=ChapterSerializer     


