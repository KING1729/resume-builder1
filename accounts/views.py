from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from user.models import Details
from login.form import detailForm
from django.http import HttpResponse
# Create your views here.
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']

        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        print("user created")
        if x is None:
            return redirect('register')
        else:
            return redirect('login')
            #form = detailForm
            #return render(request,'make.html',{'form': form,'username1':username})
    else:
        return render(request,'register.html')

def make(request):
    submitted = False
    if request.method=="POST":
        form=detailForm(request.POST)
        if form.is_valid():
            form.save()
            details = Details.objects.get(username='username1')
            return render(request, 'index1.html', {'details': details})
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
                return render(request,'make.html',{'form':form})

def build(request):
    return render(request,'build.html')

