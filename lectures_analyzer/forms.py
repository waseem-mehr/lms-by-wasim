from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Subject
from .models import Cls
from django import forms
from .models import Teacher
from .models import Lecture
class TeacherForm(ModelForm):
    class Meta:
        model=Teacher
        fields=['name','email','cell']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'cell':forms.TextInput(attrs={'class':'form-control'}),
        }

class LectureForm(ModelForm):
    class Meta:
        model=Lecture
        fields=['subject_name','class_name','teacher_name','date','status']
        widgets={
            'status':forms.Select(attrs={'class':'form-control'}),
            'subject_name':forms.Select(attrs={'class':'form-control'}),
            'class_name':forms.Select(attrs={'class':'form-control'}),
            'teacher_name':forms.Select(attrs={'class':'form-control'}),
            'date':forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1','placeholder':'format : 2020-06-29 15:58:58'})
        }

class ClsForm(ModelForm):
    class Meta:
        model=Cls
        fields=['faculty_name','cls_name']
        widgets={
            'faculty_name':forms.TextInput(attrs={'class':'form-control'}),
            'cls_name':forms.TextInput(attrs={'class':'form-control'})
        }

class SubjectForm(ModelForm):
    class Meta:
        model=Subject
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'})
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' :forms.TextInput(attrs={'class': 'form-control'}),

        }