from rest_framework import serializers 
from . import models 

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['id', 'full_name', 'email', 'password', 'qualification', 'detail','mobile_no', 'skills', 'teacher_courses', 'skill_list', 'profile_img']
    
              
    def __init__(self, *args, **kwargs):
        super(TeacherSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0 
        if request and request.method == 'GET':
            self.Meta.depth = 1  



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseCategory
        fields=['id', 'title', 'description']        


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Course
        fields=['id', 'category', 'teacher', 'title', 'description',
         'featured_img', 'technology', 'course_chapters',
          'related_videos', 'tech_list', 'total_enrolled_students', 'course_rating']    
        
            
    def __init__(self, *args, **kwargs):
        super(CourseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0 
        if request and request.method == 'GET':
            self.Meta.depth = 1  


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Chapter
        fields=['id', 'course', 'title', 'description', 'video', 'remarks']  

        
    def __init__(self, *args, **kwargs):
        super(ChapterSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0 
        if request and request.method == 'GET':
            self.Meta.depth = 1  


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields=['id', 'full_name', 'email', 'username', 'password', 'interested_categories']


class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.StudentCourseEnrollment
        fields=['id', 'course', 'student', 'enrolled_time']        
        depth=1

    def __init__(self, *args, **kwargs):
        super(StudentCourseEnrollSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0 
        if request and request.method == 'GET':
            self.Meta.depth = 1  
    

class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseRating
        fields=['id', 'course', 'student', 'rating', 'reviews', 'review_time']

    def __init__(self, *args, **kwargs):
        super(CourseRatingSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0 
        if request and request.method == 'GET':
            self.Meta.depth = 1  

class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields=['total_teacher_courses','total_teacher_students', 'total_teacher_chapters']


    