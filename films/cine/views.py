from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from cine.models import Cine
from .forms import Cineform




def home(request):
    k = Cine.objects.all()

    return render(request, 'home.html', {'c': k})
# Create your views here.

def addfilms(request):
    if (request.method == "POST"):
        n = request.POST['n']
        d = request.POST['d']
        y = request.POST['y']
        i = request.FILES['i']

        c = Cine.objects.create(name=n, desc=d, year=y,img=i)
        c.save()
        return home(request)
    return render(request, 'addfilms.html')


def filmdetail(request,p):
    c=Cine.objects.get(id=p)
    return render(request,'edit.html',{'c':c})


def filmedit(request,p):
    c = Cine.objects.get(id=p)
    if (request.method == "POST"):  # After form submission
        form = Cineform(request.POST,request.FILES,instance=c)  # Creates form object initialized with values inside request.POST
        if form.is_valid():
            form.save()  # saves the form object inside Db table
        return home(request)

    form=Cineform(instance= c)
    return render (request,'change.html',{'form':form})



def filmdelete(request,p):
    c=Cine.objects.get(id=p)
    c.delete()
    return home(request)
