from django.shortcuts import render
from . forms import StudentRegistration
from django.http import HttpResponse
from  . forms import *
from . models import Student
from . models import User
from . models import *

# Create your views here.

def showformdata(request):

    if request.method == 'POST':

        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            mb = fm.cleaned_data['mobile']
            pw = fm.cleaned_data['password']

            reg = User(name=nm, email=em, mobile=mb, password=pw)
            reg.save()
    else:
            fm = StudentRegistration()
    return render(request, 'userregistration.html', {'form': fm})


def studentinfo(request):
    stud = Student.objects.all()
    print('My_output', stud)
    return render(request, 'studetails.html', {'stu': stud})


def website(request):
    return render(request, 'index.html')
