import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

now = datetime.datetime.now()

def index(request): # Function who represent the view
	return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })