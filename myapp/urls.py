
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('Student', views.student, name='Student'),
    path('Vehicle/', views.vehicle, name='Vehicle'),
    path('Teachers/', views.teacher_list, name='Teacher'),
    path('Contact/', views.contact_us, name='Contact Us'),
    path('Home/', views.index, name='Home'),
    # path('collect_client_data/', views.collect_client_data, name='collect_client_data'),
    path('success/', views.success, name='success'),
    path('client_form/', views.client_form, name='client_form'),
]
