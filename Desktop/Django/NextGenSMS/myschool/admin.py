from django.contrib import admin
from .models import Area, Subject, Level, Grade, StaffType, StaffProfile, GradeParallel, Student, Attendance, SubjectGrade, ScoreRecord

# Register your models here.
admin.site.register(Area)
admin.site.register(Subject)
admin.site.register(Level)
admin.site.register(Grade)
admin.site.register(StaffType)
admin.site.register(StaffProfile)
admin.site.register(GradeParallel)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(SubjectGrade)
admin.site.register(ScoreRecord)
