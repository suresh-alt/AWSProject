from django.shortcuts import render, redirect


# Create your views here.
def show(request):
    return render(request,'index.html')


def adlog(request):
    return render(request,'adminlogon.html')


def checklog(request):
    uname=request.POST.get('u1')
    passw=request.POST.get('u2')

    if uname == 'suresh' and passw == 'suresh123':
        return redirect('adhome')
    else:
        return render(request,"adminlogon.html",{"error":"invalid details"})


def adhome(request):
    return render(request,"adminhome.html")