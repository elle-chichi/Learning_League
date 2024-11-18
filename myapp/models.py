from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student.name} - {self.class_enrolled.name}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_attended = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.class_attended.name}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name


