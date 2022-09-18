from rest_framework import serializers 
from . import models 

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['id', 'full_name', 'email', 'password', 'qualification', 'detail','mobile_no', 'skills', 'teacher_courses']
        depth=1



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseCategory
        fields=['id', 'title', 'description']        


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Course
        fields=['id', 'category', 'teacher', 'title', 'description',
         'featured_img', 'technology', 'course_chapters', 'related_videos']    
        depth=1

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Chapter
        fields=['id', 'course', 'title', 'description', 'video', 'remarks']    


