from rest_framework import serializers 
from catalyst.models import Companies
 
 
class CompanySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Companies
        fields = ('id',
                  'name',
                  'domain',
                  'year_founded',
                  'industry',
                  'size_range',
                  'locality',
                  'country',
                  'linkedin_url',
                  'current_employee_estimate',
                  'total_employee_estimate')
        errors = ()          

class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Companies
        fields = ('id',
                  'username',
                  'email',
                  'is_active',
                  'password')               