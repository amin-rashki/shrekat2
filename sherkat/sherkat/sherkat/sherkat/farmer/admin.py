from django.contrib import admin
from import_export import admin as import_export_admin
from import_export import resources as import_export_resources
from . import models
from .models import Kshavarz
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin

# upload Excel
class KeshavrzImportExportResource(import_export_resources.ModelResource):
    class Meta:
        model = models.Kshavarz
        fields = (
            'id',
            'name',
            'family',
            'father',
            'kodMele',
            'phone',
            'kodEshtrak',
            'city',
            'licenseNumber',
            'dateRegistration',
            'activiityStatus',
            'rosta',
            'river',
            'chahak'
        )


class KeshavarzImportExportMixin(import_export_admin.ImportExportActionModelAdmin):
    def get_import_resource_class(self):
        return KeshavrzImportExportResource


# jalali date
@admin.register(models.Kshavarz)
class Kshavarzadmin(KeshavarzImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'father', 'kodMele',
                    'phone', 'dateRegistration']

    # show jalali date in list display
    def get_dateRegistration_jalali(self, Kshavarzadmin):
        return datetime2jalali(Kshavarzadmin.dateRegistration).strftime('%y/%m/%d _ %H:%M:%S')

    get_dateRegistration_jalali.short_description = 'تاریخ ایجاد'
    get_dateRegistration_jalali.admin_order_field = 'dateRegistration'



