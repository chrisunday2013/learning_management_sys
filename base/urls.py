from django.urls import path 
from . import views 


urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.Teacher_update_destroy_detail.as_view()),
    path('teacher-login', views.teacher_login),
    path('category/', views.CategoryList.as_view()),
    path('course/', views.CourseList.as_view()),
    path('chapter/', views.ChapterList.as_view()),
    path('chapter/<int:pk>', views.Chapter_upate_detail.as_view()),
    path('teacher-courses/<int:teacher_id>', views.TeacherCourseList.as_view()),
    path('course-chapters/<int:course_id>', views.CourseChapterList.as_view()),
    path('teacherCourse-details/<int:pk>', views.TeacherCourse_upate_detail_delete.as_view()),
]