
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('classes/', views.class_list, name='class_list'),
    path('grades/', views.grade_list, name='grade_list'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('create/', views.create_item, name='create_item'),
]
