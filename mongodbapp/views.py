from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def create(request):
    if request.method=='POST':
        a=studentForm(request.POST)
        if a.is_valid():
            a.save()
        else:pass
    else:pass
    a= studentForm()
    b = students.objects.all()
    return render(request,'index.html',{'form':a,'data':b})

# update your views here.
def update(request,Name):
    c = students.objects.get(Name = Name)
    d = students.objects.all()
    e = studentForm(instance=c)
    if request.method =='POST':
        a = studentForm(request.POST,instance=c)
        if a.is_valid():
            a.save()           
            return redirect('create')
        else:pass
    else:pass
    return render(request,'index.html',{'form':e,'data':d})

# delete your views here.
def delete(request,Name):
    f =students.objects.get(Name=Name)
    f.delete()
    return redirect('create')
    
        
    
    



    
