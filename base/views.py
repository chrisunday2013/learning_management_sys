
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import AttemptQuizSerializer, CategorySerializer, ChapterSerializer, CourseQuizSerializer, CourseRatingSerializer, CourseSerializer, NotificationSerializer, QuestionSerializer, QuizSerializer, StudentAssignmentSerializer, StudentCourseEnrollSerializer, StudentDashboardSerializer, StudentFavoriteCourseSerializer, StudentSerializer, StudyMaterialSerializer, TeacherDashboardSerializer, TeacherSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework import generics
from . import models
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4


class TeacherList(generics.ListCreateAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # pagination_class=StandardResultsSetPagination
    
    def get_queryset(self):
        if 'popular' in self.request.GET:
            sql="SELECT * ,COUNT(c.id) as total_course FROM base_teacher as t INNER JOIN base_course as c ON c.teacher_id=t.id GROUP BY t.id ORDER BY total_course desc"
        return models.Teacher.objects.raw(sql)



class Teacher_update_destroy_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer 


@csrf_exempt
def teacher_login(request):
    email=request.POST['email']
    password=request.POST['password']

    try:
        teacherData=models.Teacher.objects.get(email=email,password=password)
    except models.Teacher.DoesNotExist:   
         teacherData=None
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
    pagination_class=StandardResultsSetPagination
    
    def get_queryset(self):
        qs=super().get_queryset()
        if 'result' in self.request.GET:
            limit=int(self.request.GET['result'])
            qs=models.Course.objects.all().order_by('-id')[:limit]

        if 'category' in self.request.GET:
            category=self.request.GET['category']
            qs=models.Course.objects.filter(technology__icontains=category)    

        if 'skill_name' in self.request.GET and 'teacher' in self.request.GET:
            skill_name=self.request.GET['skill_name']
            teacher=self.request.GET['teacher']
            teacher=models.Teacher.objects.filter(id=teacher).first()
            qs=models.Course.objects.filter(technology__icontains=skill_name, teacher=teacher)    
       
        
        if 'search_id' in self.kwargs:
            search=self.kwargs['search_id']
            if search: 
                 qs=models.Course.objects.filter(Q(title__icontains=search)|Q(technology__icontains=search))    

        elif 'studentId' in self.kwargs:
            student_id=self.kwargs['studentId']
            student = models.Student.objects.get(pk=student_id)
            print(student.interested_categories)
            queries = [Q(technology__iendswith=value) for value in student.interested_categories]
            query = queries.pop()
            for item in queries:
                query !=item
            qs=models.Course.objects.filter(query)   
            return qs 
        return qs     
        

class Course_upate_detail_delete(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Course.objects.all()
    serializer_class=CourseSerializer           


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

    def get_serializer_context(self):
        context=super().get_serializer_context()
        context['chapter_duration']=self.chapter_duration
        print('context----------')
        print(context)
        return context   


class StudentList(generics.ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=StudentSerializer


@csrf_exempt
def student_login(request):
    email=request.POST['email']
    password=request.POST['password']
    try:
        studentData=models.Student.objects.get(email=email,password=password)
    except models.Student.DoesNotExist:   
         studentData=None
    if studentData:     
         return JsonResponse({'bool':True, 'student_id':studentData.id})
    else:
        return JsonResponse({'bool':False})    


class StudentEnrollCourseList(generics.ListCreateAPIView):
    queryset=models.StudentCourseEnrollment.objects.all()
    serializer_class=StudentCourseEnrollSerializer


def studentEnrolledStatus(request, student_id, course_id):
    student=models.Student.objects.filter(id=student_id).first()
    course=models.Course.objects.filter(id=course_id).first()
    enrolledStatus=models.StudentCourseEnrollment.objects.filter(course=course, student=student).count()
    if enrolledStatus:     
         return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})    
    

class EnrolledStudentList(generics.ListAPIView):
    queryset=models.StudentCourseEnrollment.objects.all()
    serializer_class=StudentCourseEnrollSerializer

    def get_queryset(self):
        if  'course_id' in self.kwargs:
            course_id=self.kwargs['course_id']
            course=models.Course.objects.get(pk=course_id)
            return models.StudentCourseEnrollment.objects.filter(course=course)
        elif 'teacher_id' in self.kwargs:
            teacher_id=self.kwargs['teacher_id']
            teacher=models.Teacher.objects.get(pk=teacher_id)
            return models.StudentCourseEnrollment.objects.filter(course__teacher=teacher).distinct()
        elif 'student_id' in self.kwargs:
            student_id=self.kwargs['student_id']
            student=models.Student.objects.get(pk=student_id)
            return models.StudentCourseEnrollment.objects.filter(student=student).distinct()
    

class CourseRatingList(generics.ListCreateAPIView):
    queryset=models.CourseRating.objects.all()
    serializer_class=CourseRatingSerializer
    pagination_class=StandardResultsSetPagination

    def get_queryset(self):
        if 'popular' in self.request.GET:
            sql="SELECT *,AVG(cr.rating) as avg_rating FROM base_courserating as cr INNER JOIN base_course as c ON cr.course_id=c.id GROUP BY c.id ORDER BY avg_rating desc Limit 4"
            return models.CourseRating.objects.raw(sql)
        if 'all' in self.request.GET:
            sql="SELECT *, AVG(cr.rating) as avg_rating FROM base_courserating as cr INNER JOIN base_course as c ON cr.course_id=c.id GROUP BY c.id ORDER BY avg_rating desc"
            return models.CourseRating.objects.raw(sql)
        return models.CourseRating.objects.filter(course__isnull=False).order_by('-rating')    
             
        # course_id=self.kwargs['course_id']
        # course = models.Course.objects.get(pk=course_id)
        # return models.CourseRating.objects.filter(course=course) 


def fetch_RatingStatus(request, student_id, course_id):
    student=models.Student.objects.filter(id=student_id).first()
    course=models.Course.objects.filter(id=course_id).first()
    ratingStatus=models.CourseRating.objects.filter(course=course, student=student).count()
    if ratingStatus:     
         return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})    


@csrf_exempt
def teacher_password_change(request, teacher_id):
    password=request.POST['password']

    try:
        teacherData=models.Teacher.objects.get(id=teacher_id)
    except models.Teacher.DoesNotExist:   
         teacherData=None
    if teacherData:  
         models.Teacher.objects.filter(id=teacher_id).update(password=password)   
         return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})    

    
class TeacherDashboard(generics.RetrieveAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherDashboardSerializer

 
class StudentDashboard(generics.RetrieveAPIView):
    queryset=models.Student.objects.all()
    serializer_class=StudentDashboardSerializer


class StudentFavoriteCourseList(generics.ListCreateAPIView):
    queryset=models.StudentFavoriteCourse.objects.all()
    serializer_class=StudentFavoriteCourseSerializer 

    
    def get_queryset(self):
       
        if 'student_id' in self.kwargs:
            student_id=self.kwargs['student_id']
            student=models.Student.objects.get(pk=student_id)
            return models.StudentFavoriteCourse.objects.filter(student=student).distinct()
       

def remove_favorite_course(request, student_id, course_id):
    student=models.Student.objects.filter(id=student_id).first()
    course=models.Course.objects.filter(id=course_id).first()
    favoriteStatus=models.StudentFavoriteCourse.objects.filter(course=course, student=student).delete()
    if favoriteStatus:     
         return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})    


def student_favorite_status(request, student_id, course_id):
    student=models.Student.objects.filter(id=student_id).first()
    course=models.Course.objects.filter(id=course_id).first()
    favoriteStatus=models.StudentFavoriteCourse.objects.filter(course=course, student=student).first()
    if favoriteStatus and favoriteStatus.status == True:  
         return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})    


class StudentAssignment(generics.ListCreateAPIView):
    queryset=models.StudentAssignment.objects.all()
    serializer_class=StudentAssignmentSerializer

    def get_queryset(self):
        student_id=self.kwargs['student_id']
        teacher_id=self.kwargs['teacher_id']
        student = models.Student.objects.get(pk=student_id)
        teacher = models.Teacher.objects.get(pk=teacher_id)
        return models.StudentAssignment.objects.filter(student=student,teacher=teacher)


class UserAssignmentList(generics.ListCreateAPIView):
    queryset=models.StudentAssignment.objects.all()
    serializer_class=StudentAssignmentSerializer

    def get_queryset(self):
        student_id=self.kwargs['student_id']
        student = models.Student.objects.get(pk=student_id)
        #update Notifications
        models.Notification.objects.filter(student=student,notif_for='student', notif_subject='assigment').update(notif_status=True)
        return models.StudentAssignment.objects.filter(student=student)        


class UpdateAssignment(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.StudentAssignment.objects.all()
    serializer_class=StudentAssignmentSerializer

class Student_update_destroy_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Student.objects.all()
    serializer_class=StudentSerializer 



@csrf_exempt
def student_password_change(request, student_id):
    password=request.POST['password']

    try:
        studentData=models.Teacher.objects.get(id=student_id)
    except models.Student.DoesNotExist:   
         studentData=None
    if studentData:  
         models.Student.objects.filter(id=student_id).update(password=password)   
         return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})  


class NotificationList(generics.ListCreateAPIView):
    queryset=models.Notification.objects.all()
    serializer_class=NotificationSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = models.Student.objects.get(pk=student_id)
        return models.Notification.objects.filter(student=student,notif_for='student', notif_subject='assignment', notif_status=False)


class QuizList(generics.ListCreateAPIView):
    queryset=models.Quiz.objects.all()
    serializer_class=QuizSerializer


class TeacherQuizList(generics.ListCreateAPIView):
    serializer_class=QuizSerializer

    def get_queryset(self):
        teacher_id=self.kwargs['teacher_id']
        teacher=models.Teacher.objects.get(pk=teacher_id)
        return models.Quiz.objects.filter(teacher=teacher)


class TeacherQuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Quiz.objects.all()
    serializer_class=QuizSerializer  


class Quiz_upate_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Quiz.objects.all()
    serializer_class=QuizSerializer  



class QuizQuestionList(generics.ListCreateAPIView):
    serializer_class=QuestionSerializer

    def get_queryset(self):
        quiz_id=self.kwargs['quiz_id']
        quiz=models.Quiz.objects.get(pk=quiz_id)
        return models.QuizQuestions.objects.filter(quiz=quiz)


class QuizQuestionList(generics.ListCreateAPIView):
    serializer_class=QuestionSerializer
    
    def get_queryset(self):
        quiz_id=self.kwargs['quiz_id']
        quiz=models.Quiz.objects.get(pk=quiz_id)
        if 'limit' in self.kwargs:
            return models.QuizQuestions.objects.filter(quiz=quiz).order_by('id')[:1]
        elif 'question_id' in self.kwargs:
            current_question=self.kwargs['question_id']
            return models.QuizQuestions.objects.filter(quiz=quiz, id__gt=current_question).order_by('id')[:1]    
        else:    
            return models.QuizQuestions.objects.filter(quiz=quiz)


class AssignQuizCourseList(generics.ListCreateAPIView):
    queryset=models.CourseQuiz.objects.all()
    serializer_class=CourseQuizSerializer

    def get_queryset(self):
        if 'course_id' in self.kwargs:
            course_id=self.kwargs['course_id']
            course = models.Course.objects.get(pk=course_id)
            return models.CourseQuiz.objects.filter(course=course)


def fetch_quiz_assign_status(request, quiz_id, course_id):
    quiz=models.Quiz.objects.filter(id=quiz_id).first()
    course=models.Course.objects.filter(id=course_id).first()
    assignStatus=models.CourseQuiz.objects.filter(course=course, quiz=quiz).count()
    if assignStatus:
        return JsonResponse({'bool':True})    
    else:
        return JsonResponse({'bool':False})   


class AttemptQuizList(generics.ListCreateAPIView):
    queryset=models.AttemptQuiz.objects.all()
    serializer_class=AttemptQuizSerializer

    def get_queryset(self):
        if 'quiz_id' in self.kwargs:
            quiz_id=self.kwargs['quiz_id']
            quiz = models.Quiz.objects.get(pk=quiz_id)
        return models.AttemptQuiz.objects.raw(f'SELECT * FROM base_attemptquiz WHERE quiz_id={int(quiz_id)} GROUP by student_id')


def fetch_quiz_attempt_status(request, quiz_id, student_id):
    quiz=models.Quiz.objects.filter(id=quiz_id).first()
    student=models.Student.objects.filter(id=student_id).first()
    attemptStatus=models.AttemptQuiz.objects.filter(student=student, question__quiz=quiz).count()
    print(models.AttemptQuiz.objects.filter(student=student, question__quiz=quiz).query) 
    if attemptStatus > 0:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})               

       
def fetch_quiz_status(request, quiz_id, student_id):
    quiz=models.Quiz.objects.filter(id=quiz_id).first()
    student=models.Student.objects.filter(id=student_id).first()
    total_questions=models.QuizQuestions.objects.filter(quiz=quiz).count()
    total_attempted_questions=models.AttemptQuiz.objects.filter(quiz=quiz,student=student).values('student').count()
    attempted_questions=models.AttemptQuiz.objects.filter(quiz=quiz, student=student)

    total_correct_questions=0
    for attempt in attempted_questions:
        if attempt.right_ans == attempt.question.right_ans:
            total_correct_questions+=1
    return JsonResponse({'total_questions':total_questions, 'total_correct_questions':total_correct_questions, 'total_attempted_questions':total_attempted_questions})  


class StudyMaterialList(generics.ListCreateAPIView):
    serializer_class=StudyMaterialSerializer
    
    def get_queryset(self):
        course_id=self.kwargs['course_id']
        course=models.Course.objects.get(pk=course_id)
        return models.StudyMaterial.objects.filter(course=course)


class StudyMaterial(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.StudyMaterial.objects.all()
    serializer_class=StudyMaterialSerializer  

def update_view(request,course_id):
    queryset=models.Course.objects.filter(pk=course_id).first()
    queryset.course_views+=1
    queryset.save()
    return JsonResponse({'views':queryset.course_views})     
  
