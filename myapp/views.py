from django.shortcuts import render
from .forms import CustomerForms
from django.http import HttpResponse
import datetime
from .views import *
from .task import *


def crispyform(request):
    """
    This is function represents to get the crispy form data
    
    """
    if request.method == "GET":
        form = CustomerForms()
        return render(request, 'myapp/customer_form.html', {'form': form})

    if request.method == "POST":
        form = CustomerForms(request.POST)

        # form.save(rest api django rest framework code keen)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.updated_at = datetime.datetime.now()
            obj.save()
            return render(request, 'myapp/customer_form.html', {'form': form})


def celerytest(request):
    """
    this function is to test the celery and the redis
    """
    sleepy.delay(10)
    return HttpResponse("<h1>Hello welcome to the celery</h1>")
