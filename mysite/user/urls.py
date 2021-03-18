from django.urls import path
from user import views

app_name = "user"
urlpatterns = [
    path("", views.index, name = "index"),
    path("sign-up/", views.UserCreationView, name = "sign-up"),
    path("logout/", views.logout, name = "logout"),
    path("change-password/", views.change_password, name = "change-password"),
    path("profile-view/", views.profile_view, name = "profile-view"),
    path("update-profile", views.update_profile, name = "update-profile"),
    path("dashboard/", views.dashboard, name = "dashboard"),
]
