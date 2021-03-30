from django.urls import path
from product import views

app_name = "product"
urlpatterns = [
    path("product-creation-page", views.productCreationView, name = "product-creation"),
    path("product-updation-page/<int:product_id>", views.productUpdationView, name = "product-updation"),
    path("product-deletion-page/<int:product_id>", views.productDeletionView, name = "product-deletion"),
    path("", views.ProductListView.as_view(), name = "product-list"),
    path("<pk>/", views.ProductDetailView.as_view(), name= "product-details"),
]
