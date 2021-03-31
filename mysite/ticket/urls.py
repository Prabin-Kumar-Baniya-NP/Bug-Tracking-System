from django.urls import path
from ticket import views


app_name = "ticket"
urlpatterns = [
    path("report-bug/", views.report_bug, name = "report-bug")
]
