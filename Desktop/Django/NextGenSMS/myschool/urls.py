from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.index, name='index'),

    # Students
    path('students/', views.students, name='students'),
    path('register_student/<int:grade_parallel_id>/', views.register_student, name='register_student'),
    path('students_by_grade_parallel/<int:grade_parallel_id>/', views.students_by_grade_parallel, name='students_by_grade_parallel'),
    path('view_student_detail/<int:grade_parallel_id>/<int:student_id>/', views.view_student_detail, name='view_student_detail'),
    path('edit_student/<int:grade_parallel_id>/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:grade_parallel_id>/<int:student_id>/', views.delete_student, name='delete_student'),

    # Attendance
    path('attendance/', views.attendance, name='attendance'),
    path('attendance_data/', views.attendance_data, name='attendance_data'),
    path('mark_attendance/<int:grade_parallel_id>/', views.mark_attendance, name='mark_attendance'),

    # Performance
    path('view_performance/<int:grade_parallel_id>/', views.view_performance, name='view_performance'),

    # Exams
    path('download_exams/<int:grade_parallel_id>/', views.download_exams, name='download_exams'),
    path('generate_exam_records/<int:grade_parallel_id>/', views.generate_exam_records, name='generate_exam_records'),
    path('upload_exam/<int:grade_parallel_id>/', views.upload_exam, name='upload_exam'),

    
    # Teachers
    path('register_teacher/', views.register_teacher, name='register_teacher'),
    path('list_teachers/', views.list_teachers, name='list_teachers'),
    path('teacher_portal/', views.teacher_portal, name='teacher_portal'),
    path('report_card/<int:student_id>/', views.generate_report_card, name='generate_report_card'),
    path('grade_parallel_report/<int:grade_parallel_id>/', views.grade_parallel_report, name='grade_parallel_report'),

    # Grade Parallel Actions
    path('grade_parallel_actions/<int:grade_parallel_id>/', views.grade_parallel_actions, name='grade_parallel_actions'),

    # Authentication
    path('login/', views.login_view, name='login'),
]
