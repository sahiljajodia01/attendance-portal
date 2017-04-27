from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportMixin
from .models import ExcelFiles
from import_export import resources, fields


class ExcelFilesResource(resources.ModelResource):

    name = fields.Field(attribute='name', column_name='Name')
    sapID = fields.Field(attribute='sapID', column_name='Sap ID')
    attendancePercent = fields.Field(attribute='attendancePercent', column_name='Attendance Percent')

    def get_instance(self, instance_loader, row):
        return False

    class Meta:
        model = ExcelFiles
        fields = ('name', 'sapID', 'attendancePercent')
        export_order = fields



class ExcelFilesAdmin(ImportExportModelAdmin , admin.ModelAdmin):
    resource_class = ExcelFilesResource
    list_display = ["name", "sapID", "attendancePercent"]
    list_display_links = ["name"]
    list_filter = ["sapID", "name"]
    search_fields = ["name", "sapID"]
    list_editable = ["attendancePercent"]

    class Meta:
        model = ExcelFiles




admin.site.register(ExcelFiles, ExcelFilesAdmin)



