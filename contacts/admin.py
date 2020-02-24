from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from contacts.models import Group, Contact

@admin.register(Group)
class ContactGroupAdmin(ImportExportModelAdmin):
    list_display = ('name', )

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('full_name', 'mobile',)
    search_fields = ('full_name', 'mobile',)