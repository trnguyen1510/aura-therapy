from django.db import models

# Create your models here.
class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    employment = models.CharField(max_length=50)
    emergency_contact_first = models.CharField(max_length=50)
    emerency_contact_last = models.CharField(max_length=50)
    emergency_contact_phone = models.CharField(max_length=15)
    emergency_contact_email = models.CharField(max_length=50)
    emergency_contact_relationship = models.CharField(max_length=30)
    insurance = models.CharField(max_length=30)
    medication = models.CharField(max_length=100)
    reason_for_going_to_therapy = models.CharField(max_length=500)

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
