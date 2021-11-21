# Generated by Django 3.2.9 on 2021-11-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('domain', models.CharField(max_length=256)),
                ('year_founded', models.FloatField(max_length=128)),
                ('industry', models.CharField(max_length=128)),
                ('size_range', models.CharField(max_length=128)),
                ('locality', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('linkedin_url', models.CharField(max_length=1024)),
                ('current_employee_estimate', models.IntegerField()),
                ('total_employee_estimate', models.IntegerField()),
            ],
        ),
    ]