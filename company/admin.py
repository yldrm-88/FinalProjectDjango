from django.contrib import admin
from .models import*

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('sirketAdi', 'sirketTarihi', 'bolum', 'sinif', 'transkript', 'konum', 'ingilizce_seviyesi', 'alan')
    list_display_links=["sirketAdi"]
    list_filter = ('sirketAdi', 'sirketTarihi', 'bolum', 'sinif', 'konum', 'ingilizce_seviyesi', 'alan')
    list_per_page=10

admin.site.register(Company,CompanyAdmin)
admin.site.register(About)