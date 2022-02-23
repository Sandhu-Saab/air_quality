from django.shortcuts import render
from django.http import HttpResponse
from  . forms import *

# Create your views here.





def contect(request):

    if request.method == 'POST':

        fm = contect(request.POST or None)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            sb = fm.cleaned_data['subject']
            ms = fm.cleaned_data['message']

            reg1 = User(name=nm, email=em, subject=sb, message=ms)
            reg1.save()
    else:
            fm = Contect()
    return render(request, 'index4.html', {'info': fm})
