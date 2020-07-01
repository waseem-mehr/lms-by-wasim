from django.urls import path
from . import views
urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('teacher/<int:id>/',views.teacher,name='teacher'),
    path('lecture/<int:id>/',views.lecture,name='lecture'),
    path('addLecture/',views.addLecture,name='addLecture'),
    path('addTeacher/',views.addTeacher,name='addTeacher'),
    path('viewTeacher/<int:id>/',views.viewTeacher,name='viewTeacher'),
    path('viewTeachers/',views.viewTeachers,name='viewTeachers'),
    path('viewLectures/',views.viewLectures,name='viewLectures'),
    path('updateTeacher/<int:id>/',views.updateTeacher,name='updateTeacher'),
    path('updateLecture/<int:id>/',views.updateLecture,name='updateLecture'),
    path('deleteLecture/<int:id>/',views.deleteLecture,name='deleteLecture'),
    path('deleteTeacher/<int:id>/',views.deleteTeacher,name='deleteTeacher'),
    path('addClass/',views.addClass,name='addClass'),
    path('addSubject/',views.addSubject,name='addSubject'),
    path('loginSignUp/',views.loginSignUp,name='loginSignUp'),
    path('login/',views.login,name='login'),
    path('logout/',views.logoutMe,name='logout')

]