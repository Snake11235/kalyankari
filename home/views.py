from django.core.mail.backends import console
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Slider, Notices, InstitutionalProfile, Services, Branch, Saving, Loan, ExchangeRate, SuccessStory


def index(request):
    slider = Slider.objects.filter(Slider_Status=True)
    notices = Notices.objects.filter(Notice_Status=True)
    ip = InstitutionalProfile.objects.all()
    services = Services.objects.filter(Services_Status=True)
    branch = Branch.objects.filter(Branch_Status=True)
    saving = Saving.objects.filter(Saving_Status=True)
    loan = Loan.objects.filter(Loan_Status=True)
    exchange = ExchangeRate.objects.filter(Exchange_Status=True)
    successstory = SuccessStory.objects.filter(Status=True)
    # for q in slider:
    #     a[q] = q.Slider_Name

    a = {'Slider': slider,
         'Notices': notices,
         'Ip': ip,
         'services': services,
         'branch': branch,
         'loan': loan,
         'exchange': exchange,
         'saving': saving,
         'successstory': successstory,
         'i': 0
         }
    return render(request, 'home/index.html', a)
