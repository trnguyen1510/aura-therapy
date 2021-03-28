
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from .models import Profile
from .forms import UserForm, ProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
@login_required()  # only logged in users should access this
def dashboard(request):
    return render(request,'dashboard.html')

def pi(request):
    pk = request.user.pk
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)
    # prepopulate UserProfileForm with retrieved user values from above.
    form = UserForm(instance=user)

    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('middlename',
                                                                        'date_of_birth',
                                                                        'address',
                                                                        'city',
                                                                        'state',
                                                                        'zip_code',
                                                                        'phone',
                                                                        'occupation',
                                                                        'emergency_contact_first',
                                                                        'emergency_contact_last',
                                                                        'emergency_contact_phone',
                                                                        'emergency_contact_email',
                                                                        'emergency_contact_relationship',
                                                                        'insurance',
                                                                        'medication',
                                                                        'reason_for_going_to_therapy',
                                                                        'Do_you_smoke',
                                                                        'alcohol',
                                                                        'Seen_therapist',
                                                                        'Married',
                                                                        'Contact_method',
                                                                        'medical_history',
                                                                        'family_history'
                                                                        ))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            form = UserForm(request.POST, instance=request.user)
            formset = ProfileInlineFormset(
                request.POST, request.FILES, instance=user)
      

            if form.is_valid():
                custom_form = form.save(commit=False)
                formset = ProfileInlineFormset(
                    request.POST, request.FILES, instance=custom_form)

                if formset.is_valid():
                    custom_form.save()
                    formset.save()
                    return redirect('dashboard')

        return render(request, "pi.html", {
            "noodle": pk,
            "noodle_form": form,
            "formset": formset,
        })
    else:
        raise PermissionDenied
        form = personform()
        return render(request, 'personal_info/pi.html', {'form': form })

def therapist(request):
    all_entries = Person.objects.all()
    relevant = Person.objects.values_list('street_address','city','state','zip_code')
    
    return render(request, 'personal_info/therapist.html', {'all_entries': all_entries})

