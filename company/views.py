from django.shortcuts import render
from .models import*
from django .db.models import Q
from .form import *
from .models import Company
from .form import StudentForm
from .predict import predict_company,get_company_info
import pandas as pd


def index(request):
    return render(request,"index.html")

def about(request):#http isteği oluşturduk.
    hakkinda=About.objects.all()
    context={
        "hakkinda":hakkinda
    }
    return render(request,"about.html",context)


def advert(request,id):
    sirket=Company.objects.filter(id=id)
    context={
        "sirket":sirket
    }
    return render(request,"advert.html",context)



def company(request):
    sirketler=Company.objects.all()
    search=""
    if request.GET.get("search"):
        search=request.GET.get("search")
        sirketler=sirketler.filter(
            Q(sirketAdi__icontains=search)
            )
    context={
        "sirketler":sirketler,
        "search":search
    }
    return render(request,"company.html",context)



def match(request):
    form = StudentForm(request.POST or None)
    result = None

    if request.method == 'POST' and form.is_valid():
        student_data = [
            form.cleaned_data['konum'],
            form.cleaned_data['bolum'],
            form.cleaned_data['sinif'],
            form.cleaned_data['transkript'],
            form.cleaned_data['ingilizce_seviyesi']
        ]
        company_id = predict_company(student_data)
        company_info = get_company_info(company_id)  # Şirket bilgilerini CSV dosyasından alıyoruz.
        result = {
           'company_id': company_id,
            'company_name': company_info.get('Sirket_isim', ''),
            'company_location': company_info.get('Konum', ''),
            'company_department': company_info.get('Bolum', ''),
            'company_class': company_info.get('Sinif', ''),
            'company_transcript': company_info.get('Transkript', ''),
            'company_english_level': company_info.get('IngilizceSeviyesi', ''),
            'konum': form.cleaned_data['konum'],
            'bolum': form.cleaned_data['bolum'],
            'sinif': form.cleaned_data['sinif'],
            'transkript': form.cleaned_data['transkript'],
            'ingilizce_seviyesi': form.cleaned_data['ingilizce_seviyesi'],

        }


    return render(request, 'match.html', {'form': form, 'result': result})

