from django.contrib import admin
from schooladmin.models import Staffs, Departments, Classes, Students, Index



# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    ist_display = ['name']

class ClassesAdmin(admin.ModelAdmin):
    list_display = ['name']

class StaffsAdmin(admin.ModelAdmin):
    list_display = ['name']

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['name']

class IndexAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'school_code', 'user_name', 'login_id']



admin.site.register(Students, StudentsAdmin)
admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Staffs, StaffsAdmin)
admin.site.register(Index, IndexAdmin)










