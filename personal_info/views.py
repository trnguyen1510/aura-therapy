from django.shortcuts import render, redirect
from .forms import personform
from .models import Person
from django.http import JsonResponse
import pandas as pd
from django.core import serializers

# Create your views here.
def pi(request):
    if request.method == 'POST':
        form = personform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
    else:
        form = personform()
        return render(request, 'personal_info/pi.html', {'form': form })

def therapist(request):
    all_entries = Person.objects.all()
    relevant = Person.objects.values_list('street_address','city','state','zip_code')
    
    return render(request, 'personal_info/therapist.html', {'all_entries': all_entries})

