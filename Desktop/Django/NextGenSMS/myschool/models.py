from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Area(models.Model):
    name = models.CharField(max_length=255, default=None, null=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255, default=None, null=True)
    abbreviation = models.CharField(max_length=10)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

class Level(models.Model):
    LEVEL_CHOICES = [
        ('Preprimary', 'Preprimary'),
        ('Primary', 'Primary'),
        ('Junior-school', 'Junior-school'),
    ]
    name = models.CharField(max_length=255, default=None, choices=LEVEL_CHOICES)
    principle = models.TextField()

    def __str__(self):
        return self.name

class Grade(models.Model):
    GRADE_CHOICES = [
        ('PP1-PP2', 'PP1-PP2'),
        ('Grade1-Grade6', 'Grade1-Grade6'),
        ('Grade7-Grade9', 'Grade7-Grade9'),
    ]
    LEVEL_CHOICES = [
        ('Preprimary', 'Preprimary'),
        ('Primary', 'Primary'),
        ('Junior-school', 'Junior-school'),
    ]
    name = models.CharField(max_length=255, choices=GRADE_CHOICES)
    level = models.CharField(max_length=255, choices=LEVEL_CHOICES)
    observation = models.TextField()

    def __str__(self):
        return self.name

class StaffType(models.Model):
    STAFF_TYPE_CHOICES = [
        ('Administrator', 'Administrator'),
        ('Teacher', 'Teacher'),
        ('Support', 'Support'),
    ]
    name = models.CharField(max_length=255, default=None, choices=STAFF_TYPE_CHOICES)

    def __str__(self):
        return self.name

class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=255)
    sex = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])
    national_id_no = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)
    address = models.TextField()
    date_of_hiring = models.DateField(default=timezone.now)
    years_of_service = models.IntegerField(default=0)
    formation = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.user.username

class GradeParallel(models.Model):
    GRADE_PARALLEL_CHOICES = [
        ('PP1', 'PP1'),
        ('PP2', 'PP2'),
        ('Grade1', 'Grade1'),
        ('Grade2', 'Grade2'),
        ('Grade3', 'Grade3'),
        ('Grade4', 'Grade4'),
        ('Grade5', 'Grade5'),
        ('Grade6', 'Grade6'),
        ('Grade7', 'Grade7'),
        ('Grade8', 'Grade8'),
        ('Grade9', 'Grade9'),
    ]
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, choices=GRADE_PARALLEL_CHOICES)

    def __str__(self):
        return self.name

class Student(models.Model):
    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    BOARDER_DAY_CHOICES = [
        ('day', 'day'),
        ('boarder', 'boarder'),
    ]
    TRANSPORT_CHOICES = [
        ('School_bus', 'School_bus'),
        ('foot', 'foot'),
        ('motorbike', 'motorbike'),
    ]
    grade_parallel = models.ForeignKey(GradeParallel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    location = models.CharField(max_length=100)
    parent_contacts = models.CharField(max_length=100)
    boarder_or_day = models.CharField(max_length=10, choices=BOARDER_DAY_CHOICES)
    means_of_transport = models.CharField(max_length=10, choices=TRANSPORT_CHOICES)
    route = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.date}"

class SubjectGrade(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade.name} - {self.subject.name}"

class ScoreRecord(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    first_term = models.IntegerField()
    second_term = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"

class StudentPerformance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    performance_metric = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade_parallel = models.ForeignKey(GradeParallel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.student} - {self.performance_metric} - {self.score}"

class Exam(models.Model):
    TERM_CHOICES = [
        ('Term 1', 'Term 1'),
        ('Term 2', 'Term 2'),
        ('Term 3', 'Term 3'),
    ]
    term = models.CharField(max_length=10, choices=TERM_CHOICES)
    date = models.DateField()
    grade_parallel = models.ForeignKey(GradeParallel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.performance_metric} - {self.score}"


class ExamScore(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.student} - {self.performance_metric} - {self.score}"


class ReportCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.CharField(max_length=10)
    total_score = models.FloatField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.student} - {self.performance_metric} - {self.score}"


class TermReport(models.Model):
    grade_parallel = models.ForeignKey(GradeParallel, on_delete=models.CASCADE)
    term = models.CharField(max_length=10)
    average_score = models.FloatField()
    highest_score = models.FloatField()
    lowest_score = models.FloatField()

    def __str__(self):
        return f"{self.student} - {self.performance_metric} - {self.score}"

