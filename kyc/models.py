import datetime

from django.db import models
from django.forms import ModelForm
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html

# Create your models here.
from django.utils.safestring import mark_safe


class Kyc(models.Model):
    FirstName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50,blank=True)
    LastName = models.CharField(max_length=50)
    Saving = 'S'
    Fixed = 'F'
    Other = 'O'
    AccountType_CHOICES = [
        (Saving, 'Saving'),
        (Fixed, 'Fixed Deposit'),
        (Other, 'Other'),
    ]
    AccountType = models.CharField(
        max_length=1,
        choices=AccountType_CHOICES,
        default=Saving,
    )
    Single = 'S'
    Joint = 'J'

    AccountOperation_CHOICES = [
        (Single, 'Single'),
        (Joint, 'Joint'),
        (Other, 'Other'),
    ]
    AccountOperation = models.CharField(max_length=1, choices=AccountOperation_CHOICES, default=Single, null=False, blank=False)
    Gender = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ],
                            default='M',
                            null=False,
                            blank=False)
    Marital_Status = models.CharField(max_length=1, choices=[
        ('M', 'Married'),
        ('U', 'Unmarried'),
    ], default='M', null=False, blank=False)
    FatherName = models.CharField(max_length=50, blank=True)
    MotherName = models.CharField(max_length=50, blank=True)
    GrandFatherName = models.CharField(max_length=50, blank=True)
    SpouseName = models.CharField(max_length=50, blank=True)
    DOB_AD = models.DateField(default=datetime.date.today(), auto_now_add=False)
    DOB_BS = models.DateField(default=datetime.date.today(), auto_now_add=False)
    Occupation = models.CharField(max_length=50, blank=True)
    OrganizationName = models.CharField(max_length=50, blank=True)
    SpouseName = models.CharField(max_length=50, blank=True)
    P_Country = models.CharField(max_length=50)
    P_Zone = models.CharField(max_length=50)
    P_District = models.CharField(max_length=50)
    P_VDC = models.CharField(max_length=50)
    P_Tole = models.CharField(max_length=50, blank=True)
    P_Ward = models.CharField(max_length=50, blank=True)
    P_House = models.CharField(max_length=50, blank=True)
    P_Phone = models.CharField(max_length=50, blank=True)
    P_Mobile = models.CharField(max_length=50)
    P_OfficePhone = models.CharField(max_length=50, blank=True)
    P_Email = models.EmailField(max_length=50, blank=True)
    T_Country = models.CharField(max_length=50, blank=True)
    T_Zone = models.CharField(max_length=50, blank=True)
    T_District = models.CharField(max_length=50, blank=True)
    T_VDC = models.CharField(max_length=50, blank=True)
    T_Tole = models.CharField(max_length=50, blank=True)
    T_Ward = models.CharField(max_length=50, blank=True)
    T_House = models.CharField(max_length=50, blank=True)
    T_Phone = models.CharField(max_length=50, blank=True)
    T_Mobile = models.CharField(max_length=50, blank=True)
    T_OfficePhone = models.CharField(max_length=50, blank=True)
    T_Email = models.EmailField(max_length=50, blank=True)
    GuardianName = models.CharField(max_length=50, blank=True)
    GuardianRelation = models.CharField(max_length=50, blank=True)
    GuardianAddress = models.CharField(max_length=50, blank=True)
    GuardianTelephone = models.CharField(max_length=50, blank=True)
    NomineeName = models.CharField(max_length=50, blank=True)
    NomineeRelation = models.CharField(max_length=50, blank=True)
    NomineeAddress = models.CharField(max_length=50, blank=True)
    NomineeTelephone = models.CharField(max_length=50, blank=True)
    NomineeMembershipno = models.CharField(max_length=50, blank=True)
    ApplicantSignature = models.ImageField(blank=True)
    AccountPhoto = models.ImageField(blank=True)

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.AccountPhoto))

    image_tag.short_description = 'Image'
    AccountFingerL = models.ImageField(blank=True)

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.AccountFingerL))

    image_tag.short_description = 'Image'
    AccountFingerR = models.ImageField(blank=True)


def image_tag(self):
    return mark_safe('<img src="/directory/%s" width="150" height="150" />' % (self.AccountFingerR))


image_tag.short_description = 'Image'


class KycForm(ModelForm):
    class Meta:
        model = Kyc
        fields = [
            'FirstName', 'MiddleName', 'LastName','AccountType',
            'AccountOperation', 'Marital_Status', 'Gender',
            'FatherName', 'MotherName', 'GrandFatherName', 'SpouseName', 'DOB_AD', 'DOB_BS',
            'OrganizationName', 'SpouseName', 'P_Country', 'P_Zone', 'P_District', 'P_VDC',
            'Occupation', 'P_Tole', 'P_Ward', 'P_House', 'P_Phone', 'P_Mobile', 'P_OfficePhone',
            'P_Email', 'T_Country', 'T_Zone', 'T_District', 'T_VDC',
             'T_Tole', 'T_Ward', 'T_House', 'T_Phone', 'T_Mobile', 'T_OfficePhone',
            'T_Email', 'GuardianName','GuardianRelation', 'GuardianAddress','GuardianTelephone', 'NomineeName',
            'NomineeRelation', 'NomineeAddress', 'NomineeTelephone', 'NomineeMembershipno', 'ApplicantSignature',
            'AccountPhoto','AccountFingerL','AccountFingerR']

