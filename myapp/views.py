from django.shortcuts import render, redirect
from .models import Student, Class, Grade, Attendance, Teacher
from .forms import StudentForm, ClassForm, GradeForm, AttendanceForm, TeacherForm

# Create your views here.

def home(request):
    context = {
        'welcome_message': "Welcome to the Learning League!",
    }
    return render(request, 'home.html')
def student_list(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            form = StudentForm()
        return render(request, 'student_list.html', {'students': students, 'form': form})

def class_list(request):
    classes = Class.objects.all()
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
        else:
            form = ClassForm()
        return render(request, 'class_list.html', {'classes': classes, 'form': form})

def grade_list(request):
    grades = Grade.objects.all()
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
        else:
            form = GradeForm()
        return render(request, 'grade_list.html', {'grades': grades, 'form': form})

def attendance_list(request):
    attendances = Attendance.objects.all()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
        else:
            form = AttendanceForm()
        return render(request, 'attendance_list.html', {'attendances': attendances, 'form': form})

def teacher_list(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        else:
            form = TeacherForm()
        return render(request, 'teacher_list.html', {'teachers': teachers, 'form': form})