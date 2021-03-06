# Generated by Django 3.2.9 on 2021-11-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='country',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='current_employee_estimate',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='domain',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='industry',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='linkedin_url',
            field=models.CharField(default='', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='locality',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='name',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='size_range',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='total_employee_estimate',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='companies',
            name='year_founded',
            field=models.FloatField(default=0, max_length=128, null=True),
        ),
    ]
