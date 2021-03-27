from django.shortcuts import render

# Create your views here.
def pi(request):
    return render(request, 'personal_info/pi.html')

def therapist(request):
    return render(request, 'personal_info/therapist.html')

