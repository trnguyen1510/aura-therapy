from django.shortcuts import render, redirect
from .forms import personform
from .models import Person

# Create your views here.
def pi(request):
    if request.method == 'POST':
        form = personform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("personal_info/pi.html")
    else:
        form = personform()
    return render(request, 'personal_info/pi.html', {'form': form })

def therapist(request):
    return render(request, 'personal_info/therapist.html')

