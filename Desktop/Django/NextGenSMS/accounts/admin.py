from django.contrib import admin
from .models import Area, Subject, Level, Grade, StaffType, StaffProfile, GradeParallel, Student, Attendance, SubjectGrade, ScoreRecord, StudentPerformance, Exam

# Register your models here.
admin.site.register(Area)
admin.site.register(Subject)
admin.site.register(Level)
admin.site.register(Grade)
admin.site.register(StaffType)
admin.site.register(StaffProfile)  # Changed from Staff to StaffProfile
admin.site.register(GradeParallel)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(SubjectGrade)
admin.site.register(ScoreRecord)
admin.site.register(StudentPerformance)
admin.site.register(Exam)
