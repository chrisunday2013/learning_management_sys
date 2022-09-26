from django.urls import path 
from . import views 


urlpatterns = [
    path('teacher', views.TeacherList.as_view()),
    path('teacher/<int:pk>', views.Teacher_update_destroy_detail.as_view()),
    path('teacher-login', views.teacher_login),
    path('category/', views.CategoryList.as_view()),
    path('course/', views.CourseList.as_view()),
    path('course/<int:pk>', views.Course_upate_detail_delete.as_view()),
    path('chapter/', views.ChapterList.as_view()),
    path('chapter/<int:pk>', views.Chapter_upate_detail.as_view()),
    path('teacher-courses/<int:teacher_id>', views.TeacherCourseList.as_view()),
    path('course-chapters/<int:course_id>', views.CourseChapterList.as_view()),
    path('teacherCourse-details/<int:pk>', views.TeacherCourse_upate_detail_delete.as_view()),
    path('student/', views.StudentList.as_view()),
    path('student-login', views.student_login),
    path('studentCourse-enrolled/', views.StudentEnrollCourseList.as_view()),
    path('fetchEnroll-status/<int:student_id>/<int:course_id>', views.studentEnrolledStatus),
    path('fetchEnrolled-students/<int:course_id>', views.EnrolledStudentList.as_view()),
    path('course-rating/<int:course_id>', views.CourseRatingList.as_view()),
    path('fetch-rating-status/<int:student_id>/<int:course_id>', views.fetch_RatingStatus),
    path('fetch-all-Enrolled-students/<int:teacher_id>', views.EnrolledStudentList.as_view()),
    path('teacher/change-password/<int:teacher_id>', views.teacher_password_change),
    path('teacher/dashboard/<int:pk>', views.TeacherDashboard.as_view()),
    path('fetch-Enrolled-courses/<int:student_id>', views.EnrolledStudentList.as_view()),
]