from django.db import models



class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=15)
    skills=models.TextField()

    class Meta:
        verbose_name_plural="1. Teachers"

    def __str__(self):
        return self.full_name    
    


class CourseCategory(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    class Meta:
        verbose_name_plural="2. Course Categories"

    def __str__(self):
        return self.title    


class Course(models.Model):
    category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    featured_img=models.ImageField(upload_to='course_imgs/', null=True)
    technology=models.TextField(null=True)

    class Meta:
        verbose_name_plural="3. Courses"


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
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=18)
    address=models.TextField()  
    interested_categories=models.TextField()

    class Meta:
        verbose_name_plural="5. Students"

    def __str__(self):
        return self.full_name   
    
    
