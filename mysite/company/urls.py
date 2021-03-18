from django.urls import path
from company import views

app_name = "company"
urlpatterns = [
    path("company-creation-page", views.companyCreationView, name = "company-creation"),
]
