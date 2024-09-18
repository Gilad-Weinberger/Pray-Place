from django.shortcuts import render
from .models import Pray, Event
import random

def home(request):
    return render(request, 'base/home.html')

def pray(request):
    pray = Pray.objects.order_by('?').first()

    context = {
        'pray': pray
    }

    return render(request, 'base/pray.html', context)