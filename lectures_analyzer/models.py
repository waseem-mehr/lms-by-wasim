from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=40, null=True)
    cell = models.CharField(max_length=40, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Cls(models.Model):
    faculty_name = models.CharField(max_length=100, null=True)
    cls_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.cls_name


class Lecture(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Not Delivered', 'Not Delivered')
    )
    subject_name = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    class_name = models.ForeignKey(Cls, null=True, on_delete=models.SET_NULL)
    teacher_name = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    def __str__(self):
        return str(self.subject_name)
