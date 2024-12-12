from django import forms
from .models import Client


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'number', 'email', 'message']

# class ClassForm(forms.ModelForm):
#     class Meta:
#         model = Class
#         fields = ['name', 'description']
#
# class TeacherForm(forms.ModelForm):
#     class Meta:
#         model = Teacher
#         fields = ['name', 'subject', 'email']
#
# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ['name', 'description']
#
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'number', 'email', 'message']
