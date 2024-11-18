"""
URL configuration for theLearningLeague project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('myapp/', include('myapp.urls')),
    path('create/',views.create_item,name='create_item'),
    path('students/', include('myapp.urls')),
    path('grades/', include('myapp.urls')),
    path('classes/', include('myapp.urls')),
    path('attendance/', include('myapp.urls')),
    path('teachers/', include('myapp.urls')),

]
