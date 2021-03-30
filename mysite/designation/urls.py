from django.urls import path
from designation import views

app_name = "designation"
urlpatterns = [
    path("designation-creation-page", views.designationCreationView, name = "designation-creation"),
    path("designation-updation-page/<int:designation_id>", views.designationUpdationView, name = "designation-updation"),
    path("designation-deletion-page/<int:designation_id>", views.designationDeletionView, name = "designation-deletion"),
    path("", views.DesignationListView.as_view(), name = "designation-list"),
    path("<pk>/", views.DesignationDetailView.as_view(), name= "designation-details"),
]
