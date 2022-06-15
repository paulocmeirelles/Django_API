from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse

def jsonEmployee(request):

    employee = list(Employee.objects.values("name","email","department"))

    return JsonResponse(employee, safe=False)

def index(request):

    return render(request,"index.html")