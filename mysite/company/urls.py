from django.urls import path
from company import views

app_name = "company"
urlpatterns = [
    path("company-creation-page", views.companyCreationView, name = "company-creation"),
    path("company-updation-page/<int:company_id>", views.companyUpdationView, name = "company-updation"),
    path("company-deletion-page/<int:company_id>", views.companyDeletionView, name = "company-deletion"),
    path("", views.CompanyListView.as_view(), name = "company-list"),
    path("<pk>/", views.CompanyDetailView.as_view(), name= "company-details"),
]
