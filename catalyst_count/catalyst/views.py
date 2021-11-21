from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from catalyst.models import AuthUsers, Companies
from catalyst.serializers import CompanySerializer, UserSerializer
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET'])
def retrieve_companies(request):
    if request.method == 'GET':
        catalyst = Companies.objects.all()
        
        search_term = request.GET.get('search_term')
        industry = request.GET.get('industry')
        year_founded = request.GET.get('year_founded')
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')
        current_employee_estimate = request.GET.get('current_employee_estimate')
        total_employee_estimate = request.GET.get('total_employee_estimate')
        
        if search_term is not None:
            catalyst = catalyst.filter(name__contains=search_term)
        
        if industry is not None:
            catalyst = catalyst.filter(industry__contains=industry)
        
        if year_founded is not None:
            catalyst = catalyst.filter(year_founded__contains=year_founded)
        
        if city is not None:
            catalyst = catalyst.filter(locality__contains=city)
        
        if state is not None:
            catalyst = catalyst.filter(locality__contains=state)
        
        if country is not None:
            catalyst = catalyst.filter(country__contains=country)
        
        if current_employee_estimate is not None:
            catalyst = catalyst.filter(current_employee_estimate__contains=current_employee_estimate)
        
        if total_employee_estimate is not None:
            catalyst = catalyst.filter(total_employee_estimate__contains=total_employee_estimate)
        
        count = catalyst.count()
        context = {
            "count": count
        }
        catalyst_serializer = CompanySerializer(catalyst, many=True)
        return render(request, 'index.html', context)
    else:
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET'])
def retrieve_users(request):
    if request.method == 'GET': 
        users = AuthUsers.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    else: 
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def retrieve_lovs(request):
    if request.method == 'GET':
        column_name = request.GET.get('column_name')
        catalyst = Companies.objects.values_list(column_name, flat=True).order_by(column_name).distinct()
        context = {
            "values": list(map(str, catalyst)), 
        }
        return render(request, 'index.html', )
    else:
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)
