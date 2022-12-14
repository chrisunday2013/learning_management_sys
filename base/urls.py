from django.urls import path 
from . import views 


urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('verify-teacher/<int:teacher_id>/', views.verifyTeacherOTP),
    path('teacher-forgot-password/', views.teacherForgotPassword),
    path('teacher-reset-password/<int:teacher_id>/', views.teacherResetPassword),

    path('student-forgot-password/', views.studentForgotPassword),
    path('student-reset-password/<int:student_id>/', views.studentResetPassword),

    path('contact/', views.ContactList.as_view()),
    path('teacher/<int:pk>', views.Teacher_update_destroy_detail.as_view()),
    path('teacher-login', views.teacher_login),
    path('category/', views.CategoryList.as_view()),
    path('popular-teachers/', views.TeacherList.as_view()),
    path('course/', views.CourseList.as_view()),
    path('course/<int:pk>', views.Course_upate_detail_delete.as_view()),
    path('chapter/', views.ChapterList.as_view()),
    path('chapter/<int:pk>', views.Chapter_upate_detail.as_view()),
    path('teacher-courses/<int:teacher_id>', views.TeacherCourseList.as_view()),
    path('course-chapters/<int:course_id>', views.CourseChapterList.as_view()),
    path('popular-courses/' , views.CourseRatingList.as_view()),
    path('teacherCourse-details/<int:pk>', views.TeacherCourse_upate_detail_delete.as_view()),
    path('student/', views.StudentList.as_view()),
    path('verify-student/<int:student_id>/', views.VerifyStudentOtp),

    path('student-login', views.student_login),
    path('studentCourse-enrolled/', views.StudentEnrollCourseList.as_view()),
    path('fetchEnroll-status/<int:student_id>/<int:course_id>', views.studentEnrolledStatus),
    path('fetchEnrolled-students/<int:course_id>', views.EnrolledStudentList.as_view()),
    path('course-rating/', views.CourseRatingList.as_view()),
    path('fetch-rating-status/<int:student_id>/<int:course_id>', views.fetch_RatingStatus),
    path('fetch-all-Enrolled-students/<int:teacher_id>', views.EnrolledStudentList.as_view()),
    path('teacher/change-password/<int:teacher_id>', views.teacher_password_change),
    path('student/change-password/<int:student_id>', views.student_password_change),
    path('teacher/dashboard/<int:pk>', views.TeacherDashboard.as_view()),
    path('fetch-Enrolled-courses/<int:student_id>', views.EnrolledStudentList.as_view()),
    path('student-add-fav-course', views.StudentFavoriteCourseList.as_view()),
    path('student-remove-fav-course/<int:course_id>/<int:student_id>', views.remove_favorite_course),
    path('fetch-fav-status/<int:student_id>/<int:course_id>', views.student_favorite_status),
    path('fetch-fav-courses/<int:student_id>', views.StudentFavoriteCourseList.as_view()),
    path('student-assignment/<int:teacher_id>/<int:student_id>', views.StudentAssignment.as_view()),
    path('user-assignment/<int:student_id>', views.UserAssignmentList.as_view()),
    path('update-assignment/<int:pk>', views.UpdateAssignment.as_view()),
    path('student/dashboard/<int:pk>', views.StudentDashboard.as_view()),
    path('student/<int:pk>', views.Student_update_destroy_detail.as_view()),
    path('student/fetch-all-notifications/<int:student_id>', views.NotificationList.as_view()),
    path('save-notification/', views.NotificationList.as_view()),

    path('student-testimonial/', views.CourseRatingList.as_view()),

    path('quiz/', views.QuizList.as_view()),
    path('show-quiz/<int:teacher_id>', views.TeacherQuizList.as_view()),
    path('teacherQuiz-detail/<int:pk>', views.TeacherQuizDetail.as_view()),
    path('quiz/<int:pk>', views.Quiz_upate_detail.as_view()),
    path('quiz-questions/<int:quiz_id>', views.QuizQuestionList.as_view()),
    path('quiz-questions/<int:quiz_id>/<int:limit>', views.QuizQuestionList.as_view()),

    path('fetch-quiz-assign-status/<int:quiz_id>/<int:course_id>', views.fetch_quiz_assign_status),
    path('quiz-assign-course/', views.AssignQuizCourseList.as_view()),
    path('fetch-assigned-quiz/<int:course_id>', views.AssignQuizCourseList.as_view()),
    path('attempt-quiz/', views.AttemptQuizList.as_view()),
    
    path('quiz-questions/<int:quiz_id>/next-question/<int:question_id>', views.QuizQuestionList.as_view()),
    path('fetch-quiz-attempt-status/<int:quiz_id>/<int:student_id>', views.fetch_quiz_attempt_status),

    path('search-courses/<str:search_id>', views.CourseList.as_view()),

    path('study-materials/<int:course_id>', views.StudyMaterialList.as_view()),
    path('study-materials/<int:pk>', views.StudyMaterial.as_view()),
    path('user/study-materials/<int:course_id>', views.StudyMaterialList.as_view()),
    path('attempted-quiz/<int:quiz_id>', views.AttemptQuizList.as_view()),
    path('update-view/<int:course_id>', views.update_view),

    path('faq/', views.faqList.as_view()),

    path('pages/', views.FlatPagesList.as_view()),
    path('pages/<int:pk>/<str:page_slug>', views.FlatPagesDetail.as_view()),

    # path('fetch-quiz-result/<int:quiz_id_result>/<int:student_id>', views.fetch_quiz_attempt_status)

    path('send-message/<int:teacher_id>/<int:student_id>', views.teacher_student_msg),
    path('get-messages/<int:teacher_id>/<int:student_id>', views.get_teacher_student_msg.as_view()),

]

