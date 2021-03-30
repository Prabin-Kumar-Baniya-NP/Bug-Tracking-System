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
    path("add-user-in-company/<int:company_id>", views.companyUnassociatedUserProfile, name = "add-user-in-company"),
    path("assign-product-to-user/<int:product_id>", views.productUnassignedUserProfile, name = "assign-product-to-user"),
    path("assign-team-to-user/<int:team_id>", views.teamUnassignedUserProfile, name = "assign-team-to-user"),
    path("assign-designation-to-user/<int:designation_id>", views.designationUnassignedUserProfile, name = "assign-designation-to-user"),
    path("addCompanyToUserProfile/<str:username>/<int:company_id>", views.addCompanyToUserProfile, name = "add-company-to-user-profile"),
    path("addProductToUserProfile/<str:username>/<int:product_id>", views.addProductToUserProfile, name = "add-product-to-user-profile"),
    path("addTeamToUserProfile/<str:username>/<int:team_id>", views.addTeamToUserProfile, name = "add-team-to-user-profile"),
    path("addDesignationToUserProfile/<str:username>/<int:designation_id>", views.addDesignationToUserProfile, name = "add-designation-to-user-profile")
]
