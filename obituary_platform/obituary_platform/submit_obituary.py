# views.py
from django.shortcuts import render, redirect
from .models import Obituary
from obituary_platform.forms import Obituary_form # type: ignore

def submit_obituary(request):
    if request.method == 'POST':
        form = Obituary_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_obituaries')
    else:
        form = Obituary_form()
    return render(request, 'obituary_form.html', {'form': form})