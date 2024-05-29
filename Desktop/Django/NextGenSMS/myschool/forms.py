from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, Attendance, StaffProfile,ExamScore

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = [
            'user', 'name', 'date_of_birth', 'place_of_birth', 'sex', 'national_id_no',
            'mobile_phone', 'address', 'date_of_hiring', 'years_of_service', 'formation',
            'specialty', 'category', 'salary'
        ]

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'address', 'date_of_birth', 'age', 'sex', 'location', 'parent_contacts',
                  'boarder_or_day', 'means_of_transport', 'route']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'address', 'date_of_birth', 'age', 'sex', 'location', 'parent_contacts',
                  'boarder_or_day', 'means_of_transport', 'route']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'attended', 'date']

class ExamScoreForm(forms.ModelForm):
    class Meta:
        model = ExamScore
        fields = ['exam', 'student', 'subject', 'score']
