
from django.db import models
from django.core import serializers
from django.core.mail import send_mail


class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100, blank=True, null=True)
    qualification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=15)
    skills=models.TextField()
    profile_img=models.ImageField(upload_to='teacher_profile_imgs/', null=True)
    detail=models.TextField(null=True)
    verify_status=models.BooleanField(default=False)
    otp_digit=models.CharField(max_length=10, null=True)
    login_auth_otp=models.BooleanField(default=False)


    class Meta:
        verbose_name_plural="1. Teachers"


    def total_teacher_courses(self):
        total_courses=Course.objects.filter(teacher=self).count()
        return total_courses


    def skill_list(self):
         skill_list=self.skills.split(',')
         return skill_list
    

    def __str__(self):
        return self.full_name   

    
    def total_teacher_chapters(self):
        total_chapters=Chapter.objects.filter(course__teacher=self).count()
        return total_chapters

    
    def total_teacher_students(self):
        total_students=StudentCourseEnrollment.objects.filter(course__teacher=self).count()
        return total_students    
        

class CourseCategory(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    class Meta:
        verbose_name_plural="2. Course Categories"

    # total course of this category    
    def total_courses(self):
        return Course.objects.filter(category=self).count()

    def __str__(self):
        return self.title    


class Course(models.Model):
    category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='category_courses')
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_courses')
    title=models.CharField(max_length=100)
    description=models.TextField()
    featured_img=models.ImageField(upload_to='course_imgs/', null=True)
    technology=models.TextField(null=True)
    course_views=models.BigIntegerField(default=0)

    class Meta:
        verbose_name_plural="3. Courses"


    def related_videos(self):
        related_videos=Course.objects.filter(technology__icontains=self.technology)
        return serializers.serialize('json',related_videos)   

    def tech_list(self):
         tech_list=self.technology.split(',')
         return tech_list

    def total_enrolled_students(self):
        total_enrolled_students=StudentCourseEnrollment.objects.filter(course=self).count()
        return total_enrolled_students

    
    def course_rating(self):
        course_rating=CourseRating.objects.filter(course=self).aggregate(avg_rating=models.Avg('rating'))
        return course_rating['avg_rating']
    

    def __str__(self):
        return self.title    
    
 
class Chapter(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_chapters')
    title=models.CharField(max_length=150)
    description=models.TextField()
    video=models.FileField(upload_to='chapter_video/', null=True)
    remarks=models.TextField(null=True)

    class Meta:
        verbose_name_plural="4. Chapters"


class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=100, null=True, blank=True)
    profile_img=models.ImageField(upload_to='student_profile_imgs/', null=True)
    interested_categories=models.TextField()
    verify_status=models.BooleanField(default=False)
    otp_digit=models.CharField(max_length=10, null=True)
    login_auth_otp=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="5. Students"

    def __str__(self):
        return self.full_name   


    # Favorite Courses
    def favorite_courses(self):
        total_fav_courses=StudentFavoriteCourse.objects.filter(student=self).count()
        return total_fav_courses    

    # Total enrolled courses
    def enrolled_courses(self):
        enrolled_courses=StudentCourseEnrollment.objects.filter(student=self).count()
        return enrolled_courses

    # completed assignments
    def completed_assignment(self):
        complete_assign=StudentAssignment.objects.filter(student=self, student_status=True).count()
        return complete_assign  


    # pending assignment
    def pending_assignment(self):
        pend_assign=StudentAssignment.objects.filter(student=self, student_status=False).count()
        return pend_assign                  
    

class StudentCourseEnrollment(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_courses')  
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrolled_student') 
    enrolled_time=models.DateTimeField(auto_now_add=True)     

    class Meta:
        verbose_name_plural="6. Enrolled Courses"

        
    def __str__(self):
        return f"{self.course}-{self.student}"   


class CourseRating(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, null=True)  
    student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)  
    rating=models.PositiveBigIntegerField(default=0)
    reviews=models.TextField(null=True)    
    review_time=models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.course}-{self.student}-{self.rating}"  

    
    class Meta:
        verbose_name_plural="7. Course Rating"    
    

class StudentFavoriteCourse(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="8. Student Favorite Courses"

    def __str__(self):
        return f"{self.course}-{self.student}"    

  
class StudentAssignment(models.Model):
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)
    student_status=models.BooleanField(default=False, null=True)
    add_time=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural="9. Student Assignment"

    def __str__(self):
        return self.title        


class Notification(models.Model):
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE,  null=True)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    notif_subject=models.CharField(max_length=250,null=True, verbose_name='Notification Subject')
    notif_for=models.CharField(max_length=250, verbose_name='Notification For')
    notif_created_time=models.DateTimeField(auto_now_add=True)    
    notif_status=models.BooleanField(default=False, verbose_name='Notification Status')     


    class Meta:
        verbose_name_plural="10. Notification"

    
class Quiz(models.Model):
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    title=models.CharField(max_length=200, null=True)
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def assign_status(self):
        return CourseQuiz.objects.filter(quiz=self).count()

    class Meta:
        verbose_name_plural="11. Quiz"

    
    def __str__(self):
        return self.title        
    


class QuizQuestions(models.Model):
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    questions=models.CharField(max_length=200)
    ans1=models.CharField(max_length=200)    
    ans2=models.CharField(max_length=200)    
    ans3=models.CharField(max_length=200)    
    ans4=models.CharField(max_length=200)   
    right_ans=models.CharField(max_length=200)  
    add_time=models.DateTimeField(auto_now_add=True)       

    class Meta:
        verbose_name_plural="12. Quiz Questions"

    
    def __str__(self):
        return self.questions       
    

class CourseQuiz(models.Model):
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)       
    add_time=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural="13. Course Quiz" 

    
    def __str__(self):
        return self.quiz       
    

class AttemptQuiz(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    question=models.ForeignKey(QuizQuestions, on_delete=models.CASCADE, null=True)  
    right_ans=models.CharField(max_length=250, null=True)  
    add_time=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural="14. Attempted Questions" 


    
    def __str__(self):
        return self.student       
    

class StudyMaterial(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    upload=models.FileField(upload_to='study_material/', null=True)
    remarks=models.TextField(null=True)

    class Meta:
        verbose_name_plural="15. Study Materials"

    
    def __str__(self):
        return self.title        


class Fags(models.Model):
    question=models.CharField(max_length=700)    
    answer=models.TextField()

    class Meta:
        verbose_name_plural="16. FAQs"    
    
    def __str__(self):
        return self.question      
  


class Contact(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    query=models.TextField()
    add_time=models.DateTimeField(auto_now=True)

     
    def __str__(self):
        return self.query   

    def save(self, *args, **kwargs):
                
        send_mail(
            'Contact Query',
            'Here is the message.',
            'potentialsunny47@gmail.com',
            [self.email],
            fail_silently=False,
            html_message=f'<p>{self.full_name}</p><p>{self.query}</p>'
        )
        return super(Contact,self).save(*args, **kwargs)     

    class Meta:
        verbose_name_plural="17. Contact Us"


   
