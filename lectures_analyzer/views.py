from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as login_auth,logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib import messages
from .filters import LectureFilter
from .forms import ClsForm,SubjectForm
from .forms import LectureForm
from .forms import TeacherForm
from .models import Teacher
from .models import Subject
from .models import Lecture
from .models import Cls
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    teachers=Teacher.objects.all()
    lectures=Lecture.objects.all()
    total_lectures=lectures.count()
    delivered_lectures=lectures.filter(status='Delivered').count()
    pending_lectures=lectures.filter(status='Pending').count()
    teach=[]
    for teacher in teachers:
        lec=Lecture.objects.filter(teacher_name=teacher).count()
        teacher_info={
            "name":teacher.name,
            "id":teacher.id,
            "total_lectures":lec
        }
        teach.append(teacher_info)
    contxt={
        "teachers":teach,
        "lectures":lectures,
        "total_lectures":total_lectures,
        "delivered_lectures":delivered_lectures,
        "pending_lectures":pending_lectures
    }
    return render(request,'lectures_analyzer\dashboard.html',contxt)

@login_required(login_url='login')
def teacher(request,id):
    context={
        "id":id
    }
    return render(request,'lectures_analyzer\\teacher.html',context)
@login_required(login_url='login')
def lecture(request,id):
    context={
        "id":id
    }
    return render(request,'lectures_analyzer\lecture.html',context)

@login_required(login_url='login')
def addLecture(request):
    create=False
    form=LectureForm()
    if request.method=='POST':
        f=LectureForm(request.POST)
        if f.is_valid():
            f.save()
            print(create)
            create=True
    context={
        'form':form,
        'create':create
    }
    return render(request,'lectures_analyzer/addLecture.html',context)

@login_required(login_url='login')
def addTeacher(request):
    form = TeacherForm()
    er=False
    if request.method=='POST':
        t=TeacherForm(request.POST)
        if t.is_valid():
            t.save()
            er=True

    context={
        "form":form,
        'error':er
    }
    return render(request,'lectures_analyzer/addTeacher.html',context)
@login_required(login_url='login')
def viewTeacher(request,id):
    id=str(id)
    all_teacher = Teacher.objects.all()
    teacher = all_teacher.get(id=id)
    lectures=Lecture.objects.all()
    lectures=lectures.filter(teacher_name=teacher)
    total_lectures=lectures.count()
    filterForm=LectureFilter(request.POST,queryset=lectures)
    lectures=filterForm.qs
    context = {
        'teacher': teacher,
        'lectures':lectures,
        'total_lectures':total_lectures,
        'filterForm':filterForm


    }

    return render(request,'lectures_analyzer/viewTeacher.html',context)
@login_required(login_url='login')
def viewTeachers(request):
    teachers=Teacher.objects.all()
    total_teachers=teachers.count()

    teach=[]
    for teacher in teachers:
        lec=Lecture.objects.filter(teacher_name=teacher).count()
        t={
            "name":teacher.name,
            "id":teacher.id,
            "total_lectures":lec
        }
        teach.append(t)
    teacherss = set()
    for t in teachers:
        teacherss.add(t.name)

    context={
        "teachers":teach,
        "total_teachers":total_teachers,
        "teacher":teacherss,

    }
    return render(request,'lectures_analyzer/viewTeachers.html',context)
@login_required(login_url='login')
def viewLectures(request):
    lectures=Lecture.objects.all()
    total_lectures=lectures.count()
    lectureFilter=LectureFilter(request.POST,queryset=lectures)
    lectures=lectureFilter.qs
    context={
        "total_lectures":total_lectures,
        "lectures":lectures,
        'lectureFilter':lectureFilter
    }
    return render(request,'lectures_analyzer/viewLectures.html',context)
@login_required(login_url='login')
def updateTeacher(request,id):

    id=str(id)
    update=False
    t=Teacher.objects.all()
    t=t.get(id=id)
    form=TeacherForm(instance=t)
    if request.method=='POST':
        form=TeacherForm(request.POST,instance=t)
        if form.is_valid():
            form.save()
            update=True
    context={
        "form":form,
        'update':update
    }
    return render(request,'lectures_analyzer/updateTeacher.html',context)
@login_required(login_url='login')
def updateLecture(request,id):
    id = str(id)
    update = False
    t = Lecture.objects.all()
    t = t.get(id=id)
    form = LectureForm(instance=t)
    if request.method == 'POST':
        form = LectureForm(request.POST, instance=t)
        if form.is_valid():
            form.save()
            update = True
    context = {
        "form": form,
        'update': update
    }
    return render(request,'lectures_analyzer/updateLecture.html',context)

@login_required(login_url='login')
def deleteLecture(request,id):
    id=str(id)
    lec=Lecture.objects.all()
    lecture=lec.get(id=id)
    lecture.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@login_required(login_url='login')
def deleteTeacher(request,id):
    id=str(id)
    teach=Teacher.objects.all()
    teacher=teach.get(id=id)
    teacher.delete()
    return redirect('viewTeachers')


@login_required(login_url='/login/')
def addClass(request):
    form=ClsForm()
    create=False
    if request.method=='POST':
        f=ClsForm(request.POST)
        if f.is_valid():
            f.save()
            create=True


    context={
        'form':form,
        'create':create
    }
    return render(request,'lectures_analyzer/addClass.html',context)


@login_required(login_url='login')
def addSubject(request):
    form=SubjectForm
    create = False
    if request.method=='POST':
        f=SubjectForm(request.POST)
        if f.is_valid():
            f.save()
            create=True

    context={
        'form':form,
        'create':create
    }
    return render(request,'lectures_analyzer/addSubject.html',context)


def loginSignUp(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form=SignUpForm()

        if request.method=='POST':
            form=SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

        context={
            'form':form,
        }

        return render(request,'lectures_analyzer/loginSignUp.html',context)


def login(request):
    if request.user.is_authenticated:
       return redirect('dashboard')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login_auth(request,user)
                return redirect('dashboard')
            else:
                messages.warning(request, 'Username Or Password not matched.')
                return redirect('login')
        return render(request,'lectures_analyzer/login.html')

def logoutMe(request):
    logout(request)
    return redirect('login')