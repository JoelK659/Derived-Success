from django.shortcuts import render, redirect, get_object_or_404
from .forms import SessionRequestForm
from django.contrib import messages
from .models import Session
from tutors.models import Tutor

# Create your views here.
def session_request(request, slug):
    tutor = get_object_or_404(Tutor, slug=slug)
    if request.method == "POST":
        form = SessionRequestForm(request.POST)

        if form.is_valid():
            session = form.save()
            messages.success(request, ("Session request was successful"))
            return redirect('home')
    else:

        initial_data = {}

        if request.user.is_authenticated:
            initial_data = {
            "student_username": request.user.username,
            "student_name" : f"{request.user.first_name} {request.user.last_name}",
            "tutor_name" : tutor.name,
            "status" : "Pending"
            }
        form = SessionRequestForm(initial=initial_data)

    return render(request, "session_request.html", {
        'form': form,
        'tutor': tutor
    })
