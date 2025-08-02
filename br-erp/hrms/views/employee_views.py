"""
ViewSet for Employee model.
"""
from rest_framework import viewsets, filters
from ..models.employee import Employee
from ..serializers.employee_serializer import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['full_name', 'email', 'phone', 'cnic']
    ordering_fields = ['join_date', 'designation', 'department', 'status']
