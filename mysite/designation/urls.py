from django.urls import path
from designation import views

app_name = "designation"
urlpatterns = [
    path("designation-creation-page", views.designationCreationView, name = "designation-creation"),
]
