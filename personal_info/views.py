from django.shortcuts import render, redirect
from .forms import personform
from .models import Person

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
    #all_entries =  personal_info_person.objects.all()
    #print (all_entries)
    return render(request, 'personal_info/therapist.html', {'all_entries': all_entries })

