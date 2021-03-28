from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middlename = models.CharField(max_length=50, blank=True, default='')
    date_of_birth = models.DateField(auto_now=False)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=13, blank=True, default='')
    occupation = models.CharField(max_length=100, default='Occupation', blank=True)
    emergency_contact_first = models.CharField(max_length=50, default='', blank=True)
    emergency_contact_last = models.CharField(max_length=50, default='', blank=True)
    emergency_contact_phone = models.CharField(max_length=15, default='', blank=True)
    emergency_contact_email = models.CharField(max_length=50, default='', blank=True)
    emergency_contact_relationship = models.CharField(max_length=30, default='', blank=True)
    insurance = models.CharField(max_length=30)
    medication = models.CharField(max_length=100)
    reason_for_going_to_therapy = models.CharField(max_length=500, default='Unspecified')

    Do_you_smoke = (
    ("Yes", "Yes"),
    ("No", "No")
    )

    alcohol = (
    ("Daily", "Daily"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
    ("Not a drinker", "Not a drinker"),
    )

    Seen_therapist = (
    ("Yes", "Yes"),
    ("No", "No")
    )

    Married = (
    ("Yes", "Yes"),
    ("No", "No")
    )

    Contact_method = (
    ("Phone", "Phone"),
    ("Email", "Email")
    )

    medical_history = (
    ("Cancer", "Cancer"),
    ("Depression", "Depression"),
    ("Diabetes", "Diabetes"),
    ("Learning Disability", "Learning Disability"),
    ("ADHD", "ADHD"),
    ("Alcoholism", "Alcoholism"),
    ("Non-medicated drugs", "Non_medicated drugs"),
    ("Mental Illness", "Mental Illness"),
    ("Obesity", "Obesity"),
    )

    family_history = (
    ("Cancer", "Cancer"),
    ("Depression", "Depression"),
    ("Diabetes", "Diabetes"),
    ("Learning Disability", "Learning Disability"),
    ("ADHD", "ADHD"),
    ("Alcoholism", "Alcoholism"),
    ("Non-medicated drugs", "Non_medicated drugs"),
    ("Mental Illness", "Mental Illness"),
    ("Obesity", "Obesity"),
    )

    Do_you_smoke = models.CharField(max_length=500, default='Unspecified', choices=Do_you_smoke)
    alcohol = models.CharField(max_length=500, default='Unspecified', choices=alcohol)
    Seen_therapist = models.CharField(max_length=500, default='Unspecified', choices=Seen_therapist)
    Married = models.CharField(max_length=500, default='Unspecified', choices=Married)
    Contact_method = models.CharField(max_length=500, default='Unspecified', choices=Contact_method)
    medical_history = models.CharField(max_length=500, default='Unspecified', choices=medical_history)
    family_history = models.CharField(max_length=500, default='Unspecified', choices=family_history)
    
    
    
    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)