from django.urls import path
from team import views

app_name = "team"
urlpatterns = [
    path("team-creation-page", views.teamCreationView, name = "team-creation"),
]
