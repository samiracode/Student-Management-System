from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        labels = {
            'student_number': 'Student Number',
            'first_name' : 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study' : 'Field of Study',
            'pga' : 'GPA'
        }
        widgets = {
            'student_number' : forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-contrl'}),
            'last_name': forms.TextInput(attrs={'class': 'form-contrl'}),
            'email': forms.EmailInput(attrs={'class': 'form-contrl'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-contrl'}),
            'gpa' : forms.NumberInput(attrs={'class': 'form-control'}),
        }