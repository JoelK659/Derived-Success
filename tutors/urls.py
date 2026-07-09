from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("tutor/<slug:slug>/", views.tutor_detail, name="tutor_detail"),
    path("session/<slug:slug>/", views.session_detail, name="session_detail"),
    path("session_decline/", views.session_decline, name="session_decline"),
    path("session_confirm/", views.session_confirm, name="session_confirm"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
