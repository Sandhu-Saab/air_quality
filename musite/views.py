from django.http import HttpResponse
from django.shortcuts import render


def okk(request):
    return HttpResponse('<h1>hello</h1>')

def showformdata(request):
    if request.method == 'POST':
        global fm
        fm = StudentRegistration(request.POST)

        if fm.is_valid():
            print('Form validated')
            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            print('Password:', fm.cleaned_data['password'])
            return HttpResponse('/thanks/')

        else:
            fm = StudentRegistration()

    return render(request, 'userregistration.html')
