from django.contrib import admin
from .models import Employee, Department

admin.site.site_header = 'department Admin panel'


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'foto', 'position', 'salary', 'age', 'department', )
    search_fields = ('full_name',)
    ordering = ('id',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('id',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)