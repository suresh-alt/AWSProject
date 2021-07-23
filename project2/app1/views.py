from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request,'index.html')


def adlog(request):
    return render(request,'adminlogon.html')