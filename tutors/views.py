from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Tutor
from tutoring_sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
@login_required(login_url="login")

def dashboard(request):
    return render(request, "dashboard.html")

def home(request):
    tutors = Tutor.objects.all()

    if request.user.is_staff:
        full_name = f"{request.user.first_name} {request.user.last_name}"
        sessions = Session.objects.filter(tutor_name=full_name).exclude(status="Declined")
    else:
        sessions = Session.objects.filter(student_username=request.user.username)
    confirmed = sessions.filter(status="Confirmed").exists()
    pending = sessions.filter(status="Pending").exists()
    declined = sessions.filter(status="Declined").exists()
    # Search Code
    tutor_name = request.GET.get("tutor_name")
    if tutor_name != "" and tutor_name is not None:
        tutors = tutors.filter(name__icontains=tutor_name)

    session_name = request.GET.get("session_name")
    if session_name != "" and session_name is not None:
        sessions = sessions.filter(student_name__icontains=session_name)

    return render(request, 'tutors/home.html', {
    "tutors": tutors,
    "sessions": sessions,
    "confirmed": confirmed,
    "pending": pending,
    "declined": declined,
    })

def tutor_detail(request, slug):
    tutor = get_object_or_404(Tutor, slug=slug)
    return render(request, "tutors/tutor_detail.html", {"tutor":tutor})

def tutor_request(request, slug):
    tutor = get_object_or_404(Tutor, slug=slug)
    return render(request, "tutors/tutor_request.html", {"tutor":tutor})

def session_detail(request, slug):
    session = get_object_or_404(Session, slug=slug)
    return render(request, "tutors/session_detail.html", {"session":session})

def session_decline(request):
    if request.method == "POST":
        session_status = request.POST.get('status')
        session_reason = request.POST.get('reason')
        session_id = request.POST.get('session_id')

        try:
            session = Session.objects.get(id=session_id)
            session.status = session_status
            session.decline_reason = session_reason
            session.save()

            return JsonResponse({'message': 'updated'})

        except Session.DoesNotExist:
            return JsonResponse({'error': 'Session not found'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'invalid request'}, status=400)

def session_confirm(request):
    if request.method == "POST":
        session_status = request.POST.get('status')
        session_id = request.POST.get('session_id')

        try:
            session = Session.objects.get(id=session_id)
            session.status = session_status
            session.save()

            return JsonResponse({'message': 'updated'})

        except Session.DoesNotExist:
            return JsonResponse({'error': 'Session not found'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'invalid request'}, status=400)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")
