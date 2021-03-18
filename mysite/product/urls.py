from django.urls import path
from product import views

app_name = "product"
urlpatterns = [
    path("product-creation-page", views.productCreationView, name = "product-creation"),
]
