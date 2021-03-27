from django.shortcuts import render

# Create your views here.
def pi(request):
    return render(request, 'pi.html')

def therapist(request):
    return render(request, 'therapist.html')

