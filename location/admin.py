from django.contrib import admin
from .models import Wilaya, Commune
from import_export.admin import ImportExportModelAdmin, ExportMixin
# Register your models here.

@admin.register(Wilaya)
class WilayaAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name','relai_delivery' ,'home_delivery','active']
    list_display_links =('id',)
    list_filter = ['active']
    list_editable = ['name', 'relai_delivery','home_delivery']
    list_per_page = 30


@admin.register(Commune)
class CommuneAdmin(ImportExportModelAdmin):
    list_display = ('name','wilaya_id')

