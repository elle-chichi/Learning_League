from django import forms
from .models import Student, Class, Grade, Attendance, Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'description']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'class_enrolled', 'grade']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'class_attended', 'date', 'present']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'email']
