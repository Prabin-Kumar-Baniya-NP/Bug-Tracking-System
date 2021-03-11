from django.urls import path
from user import views

app_name = "user"
urlpatterns = [
    path("sign_up/", views.UserCreationView, name = "sign-up"),
    path("index/", views.index, name = "index"),
    path("logout/", views.logout, name = "logout"),
    path("change-password/", views.change_password, name = "change-password"),
    path("profile-view/", views.profile_view, name = "profile-view"),
    path("update-profile", views.update_profile, name = "update-profile"),
    path("dashboard/", views.dashboard, name = "dashboard"),
]
