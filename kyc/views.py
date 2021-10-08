from django.shortcuts import render
from django.http import HttpResponseRedirect
# from .forms import KycForm
from .models import KycForm

from .models import Kyc
# Create your views here.


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = KycForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/home/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = KycForm()
    return render(request, 'kyc/index.html', {'form': form})


def addkyc(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = KycForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = KycForm()
