from django.contrib import admin
from .models import Subject
from .models import Teacher
from .models import Lecture
from .models import Cls
#Register your models here.
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Cls)
admin.site.register(Lecture)

