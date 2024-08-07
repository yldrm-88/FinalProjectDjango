from django import forms

class StudentForm(forms.Form):
    konum = forms.ChoiceField(choices=[
        ('Ankara', 'Ankara'),
        ('İstanbul', 'İstanbul'),
        ('İzmir', 'İzmir'),
        ('Antalya', 'Antalya'),
        ('Bursa', 'Bursa'),
    ])
    bolum = forms.ChoiceField(choices=[
        ('Yazılım Mühendisliği', 'Yazılım Mühendisliği'),
        ('Adli Bilişim Mühendisliği', 'Adli Bilişim Mühendisliği'),
        ('Yapay Zeka ve Veri Mühendisliği', 'Yapay Zeka ve Veri Mühendisliği'),
        ('Bilgisayar Mühendisliği', 'Bilgisayar Mühendisliği'),
        ('Elektrik Elektronik Mühendisliği', 'Elektrik Elektronik Mühendisliği'),
        ('Makine Mühendisliği', 'Makine Mühendisliği'),
    ])
    sinif = forms.IntegerField(label='Sınıf')
    transkript = forms.FloatField(label='Transkript')
    ingilizce_seviyesi = forms.ChoiceField(choices=[
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    ])
