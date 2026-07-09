from django.urls import path
from . import views


urlpatterns = [
    path('session_request/<slug:slug>/', views.session_request, name="session_request"),
]
