from django.urls import path
from team import views

app_name = "team"
urlpatterns = [
    path("team-creation-page", views.teamCreationView, name = "team-creation"),
    path("team-updation-page/<int:team_id>", views.teamUpdationView, name = "team-updation"),
    path("team-deletion-page/<int:team_id>", views.teamDeletionView, name = "team-deletion"),
    path("", views.TeamListView.as_view(), name = "team-list"),
    path("<pk>/", views.TeamDetailView.as_view(), name= "team-details"),
]
