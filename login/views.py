from django.shortcuts import render, redirect
from user.models import Details
from .form import detailForm
from django.http import HttpResponseRedirect
# Create your views here.

def make(request):
    submitted = False
    if request.method=="POST":
        form=detailForm(request.POST)
        if form.is_valid():
            form.save()
            print('data submitted')
            #details=Details.objects.get(username='username')
            return render(request,'login.html')
            #return HttpResponseRedirect('/make?submitted=True')
    else:
        form = detailForm
        if submitted in request.GET:
            submitted=True
        return render(request,'login/make.html',{'form':form, 'submitted': submitted})

def login(request):
    if request.method=='POST':
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        from django.contrib import auth
        x=auth.authenticate(username=username1,password=password1)
        if x is None:
            return redirect('login')
        else:
            if Details.objects.filter(username__contains=username1):
                details=Details.objects.get(username=username1)
                return render(request, "index1.html", {'details': details})
            else:
                form=detailForm
                #return render(request,'build.html',{'form':form})
                return render(request,'make.html', {'form': form})

    else:
        return render(request,'login.html')


def build(request):
    return render(request,'build.html')





