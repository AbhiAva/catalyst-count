from django.db import models

# Create your models here.

class Companies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, default='', null=True)
    domain = models.CharField(max_length=256, default='', null=True)
    year_founded = models.FloatField(max_length=128, default=0, null=True)
    industry = models.CharField(max_length=128, default='', null=True)
    size_range = models.CharField(max_length=128, default='', null=True)
    locality = models.CharField(max_length=128, default='', null=True)
    country = models.CharField(max_length=128, default='', null=True)
    linkedin_url = models.CharField(max_length=1024, default='', null=True)
    current_employee_estimate = models.IntegerField(default=0, null=True)
    total_employee_estimate = models.IntegerField(default=0, null=True)

class AuthUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150, default='', null=True)
    email = models.CharField(max_length=254, default='', null=True)
    is_active = models.BooleanField(default=False)
    password = models.CharField(max_length=128, default='', null=True)
    class Meta:
        db_table = "auth_users"    
