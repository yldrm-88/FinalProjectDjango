from django.db import models

# Create your models here.
class Company(models.Model):
    sirketAdi = models.CharField(max_length=100, verbose_name="Şirket Adı", default="")
    sirketTarihi = models.DateField(max_length=30, verbose_name="Staj Tarihleri", default="2024-01-01")
    bolum = models.CharField(max_length=35,)
    sinif = models.IntegerField(default=0)
    transkript = models.FloatField(default=0.0)
    konum = models.CharField(max_length=30)
    ingilizce_seviyesi = models.CharField(max_length=10)
    alan = models.CharField(max_length=50)  # Alan alanını CharField olarak tanımlıyoruz
    resim = models.FileField(upload_to='afis', blank=True, null=True)
    hakkinda = models.TextField(max_length=10000, verbose_name="Hakkında", default="")

    def __str__(self):
        return self.sirketAdi

class Student(models.Model):
    name = models.CharField(max_length=100, default="")
    bolum = models.CharField(max_length=35,)
    sinif = models.IntegerField(default=0)
    transkript = models.FloatField(default=0.0)
    konum = models.CharField(max_length=30)
    ingilizce_seviyesi = models.CharField(max_length=10)
    alan = models.CharField(max_length=50)  # Varsayılan değer ekleniyor.

    def __str__(self):
        return self.name
    
class About(models.Model):
    baslik=models.CharField(max_length=100,verbose_name="Başlık")
    hakkimizda=models.TextField(max_length=2000,verbose_name="Hakkımızda")
    resim=models.FileField(upload_to='hakkimizda',blank=True,null=True)

    def __str__ (self):
        return self.baslik
    
