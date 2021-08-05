from django.shortcuts import render
from django.http import HttpResponse
from .models import Details

def home(request):
    details = Details.objects.get(username='123456789')

    return render(request,"index.html",{'details':details});