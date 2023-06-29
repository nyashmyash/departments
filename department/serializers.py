from rest_framework import serializers
from department.models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'director', 'count_employees', 'salary_employees']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'foto', 'position', 'salary', 'age', 'department']