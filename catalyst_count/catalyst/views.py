from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from catalyst.models import AuthUsers, Companies
from catalyst.serializers import CompanySerializer, UserSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        return 'hello!'
    else:
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET'])
def retrieve_companies(request):
    if request.method == 'GET':
        catalyst = Companies.objects.all()
        
        search_term = request.GET.get('search_term', None)
        industry = request.GET.get('industry', None)
        year_founded = request.GET.get('year_founded', None)
        city = request.GET.get('city', None)
        state = request.GET.get('state', None)
        country = request.GET.get('country', None)
        employees_from = request.GET.get('employees_from', None)
        employees_to = request.GET.get('employees_to', None)
        
        if search_term is not None:
            catalyst = catalyst.filter(name__contains=search_term)
        
        if industry is not None:
            catalyst = catalyst.filter(industry__contains=industry)
        
        if year_founded is not None:
            catalyst = catalyst.filter(year_founded__contains=year_founded)
        
        if city is not None:
            catalyst = catalyst.filter(city__contains=city)
        
        if state is not None:
            catalyst = catalyst.filter(state__contains=state)
        
        if country is not None:
            catalyst = catalyst.filter(country__contains=country)
        
        if employees_from is not None:
            catalyst = catalyst.filter(employees_from__contains=employees_from)
        
        if employees_to is not None:
            catalyst = catalyst.filter(employees_to__contains=employees_to)
        
        catalyst_serializer = CompanySerializer(catalyst, many=True)
        return JsonResponse(catalyst_serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def retrieve_company(request, id):
    if request.method == 'GET':
        catalyst = Companies.objects.all()
        
        search_term = request.GET.get('search_term', None)
        industry = request.GET.get('industry', None)
        year_founded = request.GET.get('year_founded', None)
        city = request.GET.get('city', None)
        state = request.GET.get('state', None)
        country = request.GET.get('country', None)
        employees_from = request.GET.get('employees_from', None)
        employees_to = request.GET.get('employees_to', None)
        
        if search_term is not None:
            catalyst = catalyst.filter(name__contains=search_term)
        
        if industry is not None:
            catalyst = catalyst.filter(industry__contains=industry)
        
        if year_founded is not None:
            catalyst = catalyst.filter(year_founded__contains=year_founded)
        
        if city is not None:
            catalyst = catalyst.filter(city__contains=city)
        
        if state is not None:
            catalyst = catalyst.filter(state__contains=state)
        
        if country is not None:
            catalyst = catalyst.filter(country__contains=country)
        
        if employees_from is not None:
            catalyst = catalyst.filter(employees_from__contains=employees_from)
        
        if employees_to is not None:
            catalyst = catalyst.filter(employees_to__contains=employees_to)
        
        catalyst_serializer = CompanySerializer(catalyst, many=True)
        return JsonResponse(catalyst_serializer.data, safe=False)
    else:
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)
              
@api_view(['POST'])
def add_company(request):
    if request.method == 'POST':
        company_data = JSONParser().parse(request)
        company_serializer = CompanySerializer(data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse(company_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST) 
  
@api_view(['GET'])
def retrieve_users(request):
    if request.method == 'GET': 
        users = AuthUsers.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    else: 
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST) 
  
@api_view(['GET'])
def retrieve_user(request, id):
    if request.method == 'GET': 
        users = AuthUsers.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    else: 
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST) 
              
@api_view(['POST'])
def add_user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else: 
        return JsonResponse({'message': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST) 
