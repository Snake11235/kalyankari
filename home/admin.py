# Register your models here.
from django.contrib import admin

from .models import Slider, InstitutionalProfile, Services, Branch, Saving, Loan, ExchangeRate, SuccessStory, Notices

admin.site.register(Slider)
admin.site.register(InstitutionalProfile)
admin.site.register(SuccessStory)
admin.site.register(Services)
admin.site.register(Branch)
admin.site.register(Saving)
admin.site.register(ExchangeRate)
admin.site.register(Loan)
admin.site.register(Notices)