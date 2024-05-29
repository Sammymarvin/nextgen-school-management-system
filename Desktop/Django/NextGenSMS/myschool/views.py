from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from .models import Area, Subject, Level, Grade, StaffType, StaffProfile, GradeParallel, Student, Attendance, SubjectGrade, ScoreRecord, Exam, StudentPerformance, ExamScore, ReportCard, TermReport
from .forms import StudentRegistrationForm, StudentForm, AttendanceForm, ExamScoreForm, CustomAuthenticationForm, TeacherRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Avg, Max, Min, Sum

def index(request):
    grade_parallels = GradeParallel.objects.all()
    return render(request, 'index.html', {'grade_parallels': grade_parallels})

def students(request):
    grade_parallels = GradeParallel.objects.all()
    return render(request, 'students.html', {'grade_parallels': grade_parallels})

def attendance(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance.html', {'attendance_records': attendance_records})

def attendance_data(request):
    data = list(Attendance.objects.values('date', 'attended'))
    return JsonResponse(data, safe=False, encoder=DjangoJSONEncoder)

def register_student(request, grade_parallel_id):
    grade_parallel = get_object_or_404(GradeParallel, id=grade_parallel_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.grade_parallel = grade_parallel
            student.save()
            return redirect('grade_parallel_actions', grade_parallel_id=grade_parallel_id)
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form, 'grade_parallel': grade_parallel})

def students_by_grade_parallel(request, grade_parallel_id):
    grade_parallel = get_object_or_404(GradeParallel, pk=grade_parallel_id)
    students = Student.objects.filter(grade_parallel=grade_parallel)
    return render(request, 'students_by_grade_parallel.html', {'grade_parallel': grade_parallel, 'students': students})

@login_required
def view_student_detail(request, grade_parallel_id, student_id):
    grade_parallel = get_object_or_404(GradeParallel, pk=grade_parallel_id)
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'view_student_detail.html', {'student': student, 'grade_parallel': grade_parallel})

@login_required
def edit_student(request, grade_parallel_id, student_id):
    grade_parallel = get_object_or_404(GradeParallel, pk=grade_parallel_id)
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_student_detail', grade_parallel_id=grade_parallel_id, student_id=student_id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'grade_parallel': grade_parallel, 'student': student})

def grade_parallel_actions(request, grade_parallel_id):
    grade_parallel = get_object_or_404(GradeParallel, id=grade_parallel_id)
    students = Student.objects.filter(grade_parallel=grade_parallel)
    return render(request, 'grade_parallel_actions.html', {'grade_parallel': grade_parallel, 'students': students})

@login_required
def delete_student(request, grade_parallel_id, student_id):
    student = get_object_or_404(Student, id=student_id, grade_parallel_id=grade_parallel_id)
    if request.method == 'POST':
        student.delete()
        return redirect('grade_parallel_actions', grade_parallel_id=grade_parallel_id)
    return render(request, 'delete_student.html', {'student': student})

def view_performance(request, grade_parallel_id):
    grade_parallel = get_object_or_404(GradeParallel, id=grade_parallel_id)
    performance = StudentPerformance.objects.filter(grade_parallel=grade_parallel)
    students = Student.objects.filter(grade_parallel=grade_parallel)
    
    return render(request, 'combined_dashboard.html', {
        'grade_parallel_id': grade_parallel_id,
        'students': students,
        'performance': performance,
    })

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = CustomAuthenticationForm(request)
    return render(request, 'login.html', {'form': form})

@login_required
def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = User.objects.get(pk=request.POST.get('user'))
            teacher.save()
            return redirect('success_page')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'register_teacher.html', {'form': form})

@login_required
def list_teachers(request):
    teachers = StaffProfile.objects.filter(category='Teacher')
    return render(request, 'list_teachers.html', {'teachers': teachers})

@login_required
def mark_attendance(request, grade_parallel_id):
    grade_parallel = get_object_or_404(GradeParallel, pk=grade_parallel_id)
    students = Student.objects.filter(grade_parallel=grade_parallel)
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.grade_parallel = grade_parallel
            attendance.save()
            return redirect('mark_attendance', grade_parallel_id=grade_parallel_id)
    else:
        form = AttendanceForm()
    return render(request, 'mark_attendance.html', {'form': form, 'students': students, 'grade_parallel': grade_parallel})


@login_required
def download_exams(request, grade_parallel_id):
    grade_parallel = get_object_or_404(GradeParallel, pk=grade_parallel_id)
    exams = Exam.objects.filter(grade_parallel=grade_parallel)
    return render(request, 'download_exams.html', {'exams': exams, 'grade_parallel': grade_parallel})

@login_required
def generate_exam_records(request, grade_parallel_id):
    grade_parallel = get_object_or_404(GradeParallel, pk=grade_parallel_id)
    students = Student.objects.filter(grade_parallel=grade_parallel)
    scores = []
    for student in students:
        scores.append({
            'student': student,
            'exams': Exam.objects.filter(grade_parallel=grade_parallel),
        })
    return render(request, 'generate_exam_records.html', {'scores': scores, 'grade_parallel': grade_parallel})

def teacher_portal(request):
    try:
        grade_parallel = GradeParallel.objects.filter(staff=request.user.staffprofile).first()
        if grade_parallel:
            return render(request, 'teacher_portal.html', {'grade_parallel': grade_parallel})
        else:
            return render(request, 'no_grade_parallel.html')
    except GradeParallel.DoesNotExist:
        return render(request, 'no_grade_parallel.html')

from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from .models import Student, ExamScore, ReportCard

def generate_report_card(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    exams = Exam.objects.filter(grade_parallel=student.grade_parallel)
    report_cards = []

    for exam in exams:
        total_score = ExamScore.objects.filter(exam=exam, student=student).aggregate(Sum('score'))['score__sum'] or 0

        if total_score >= 76:
            comment = "Excellent work, keep it up!"
        elif 50 <= total_score < 76:
            comment = "Well done, put more effort!"
        elif 30 <= total_score < 50:
            comment = "We believe you can do better."
        else:
            comment = "Work hard, you can do better."

        # Create ReportCard object inside the loop
        report_card = ReportCard.objects.create(
            student=student,
            term=exam.term,
            total_score=total_score,
            comment=comment
        )
        
        report_cards.append(report_card)

    return render(request, 'report_card.html', {'report_cards': report_cards})

def grade_parallel_report(request, grade_parallel_id):
    grade_parallel = get_object_or_404(GradeParallel, id=grade_parallel_id)
    students = Student.objects.filter(grade_parallel=grade_parallel)
    term_reports = []

    for term in ['Term 1', 'Term 2', 'Term 3']:
        exams = Exam.objects.filter(grade_parallel=grade_parallel, term=term)
        total_scores = []
        for student in students:
            total_score = ExamScore.objects.filter(student=student, exam__in=exams).aggregate(Sum('score'))['score__sum'] or 0
            total_scores.append(total_score)

        average_score = sum(total_scores) / len(students) if students else 0
        highest_score = max(total_scores) if total_scores else 0
        lowest_score = min(total_scores) if total_scores else 0

        term_report = TermReport.objects.create(
            grade_parallel=grade_parallel,
            term=term,
            average_score=average_score,
            highest_score=highest_score,
            lowest_score=lowest_score
        )

        term_reports.append(term_report)

    return render(request, 'grade_parallel_report.html', {
        'grade_parallel': grade_parallel,
        'term_reports': term_reports,
        'students': students,
    })

@login_required
def upload_exam(request, grade_parallel_id=None):
    grade_parallels = GradeParallel.objects.all()
    exams = Exam.objects.none()  # Initialize with an empty queryset

    if grade_parallel_id:
        grade_parallel = get_object_or_404(GradeParallel, pk=grade_parallel_id)
        exams = Exam.objects.filter(grade_parallel=grade_parallel)
    else:
        grade_parallel = None

    if request.method == 'POST':
        form = ExamScoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Replace with your success URL
    else:
        form = ExamScoreForm()

    context = {
        'form': form,
        'grade_parallels': grade_parallels,
        'exams': exams,
        'selected_grade_parallel': grade_parallel
    }
    return render(request, 'upload_exam_scores.html', context)
