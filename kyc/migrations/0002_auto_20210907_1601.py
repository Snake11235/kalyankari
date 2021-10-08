# Generated by Django 3.2.7 on 2021-09-07 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='AccountOperation',
            field=models.CharField(choices=[('S', 'Single'), ('J', 'Joint'), ('O', 'Other')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='kyc',
            name='AccountType',
            field=models.CharField(choices=[('S', 'Saving'), ('F', 'Fixed Deposit'), ('O', 'Other')], default='S', max_length=1),
        ),
        migrations.AddField(
            model_name='kyc',
            name='DOB',
            field=models.DateField(default=datetime.date(2021, 9, 7)),
        ),
        migrations.AddField(
            model_name='kyc',
            name='FatherName',
            field=models.CharField(default='ERROR', max_length=50),
        ),
        migrations.AddField(
            model_name='kyc',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='kyc',
            name='GfName',
            field=models.CharField(default='ERROR', max_length=50),
        ),
        migrations.AddField(
            model_name='kyc',
            name='Marital_Status',
            field=models.CharField(choices=[('M', 'Married'), ('U', 'Unmarried')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='kyc',
            name='MotherName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='kyc',
            name='SpouseName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='FirstName',
            field=models.CharField(default='ERROR', max_length=50),
        ),
    ]