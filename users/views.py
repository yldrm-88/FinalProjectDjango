from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
#authenticate veri tabanı ile girdiğimiz bilgilerin eşit olup olmadığına bakar.
# Create your views here.
from .models import * 


def userLogin(request):
    if request.method=='POST':
        userName=request.POST["userName"]
        userPass=request.POST["userPass"]
        user=authenticate(username=userName,password=userPass)
        if user is not None:
            login(request,user)
            messages.success(request,"Giriş Başarılı")
            return redirect("company")
        else:
            messages.error(request,"Hatalı Giriş")
            return render (request,'login.html')
    return render(request,"login.html")



def register(request):
    form=UserForm()
    context={
        "form":form
    }
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
           return render(request,"register.html",context) 
    return render(request,"register.html",context)


def userLogout(request):
    logout(request)
    return redirect("index")



def iletisim(request):
        if request.method=='POST':
            contact=Contact()
            name=request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')
            contact.name=name
            contact.email=email
            contact.message=message
            contact.save()
        return render(request,'iletisim.html')


def basvur(request):
    if request.method == 'POST':
        form = BasvurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basvur')
    else:
        form = BasvurForm()
    
    context = {
        'form': form
    }
    return render(request, 'basvur.html', context)
