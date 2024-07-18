# views.py
from django.shortcuts import render
from .models import Obituary  # Assuming your model class is named Obituary

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})