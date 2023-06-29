from rest_framework import viewsets, status
from department.models import Employee, Department
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from department.serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = Employee.objects.all()
        full_name = self.request.query_params.get('full_name')
        department = self.request.query_params.get('department_id')
        if full_name is not None:
            queryset = queryset.filter(full_name__contains=full_name)

        if department is not None:
            queryset = queryset.filter(department=department)

        return queryset



