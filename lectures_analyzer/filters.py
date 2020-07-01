from django_filters import FilterSet
from django import forms
import django_filters
from .models import Lecture

class LectureFilter(FilterSet):

    class Meta:
        model=Lecture
        fields='__all__'
        exclude = ['class_name','teacher_name','date']
