from django.urls import path
from django.contrib import admin
from .api_view import EmployeeAllList, employee_get_delete, employee
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/', views.jsonEmployee, name='index'),
    path('api/employee/', employee, name='employeeJson'),
    path('api/employee/<int:pk>/', employee_get_delete, name="delete"),
]