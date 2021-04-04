from django.urls import path
from ticket import views


app_name = "ticket"
urlpatterns = [
    path("report-bug/", views.report_bug, name = "report-bug"),
    path("submitted-tickets/", views.SubmittedTicketsListView.as_view(), name = "submitted-tickets"),
    path("review-tickets/", views.reviewTickets, name = "review-tickets"),
    path("ticket-details/<int:pk>", views.TicketDetailView.as_view(), name= "ticket-details"),
    path("ticket-updation/<int:ticket_id>", views.ticketUpdation, name = "update-ticket"),
    path("assigned-tickets/", views.AssignedTicketsListView.as_view(), name = "assigned-tickets"),
    path("ticket-dashboard/<int:pk>", views.AssignedTicketDashboardDetailView.as_view(), name = "ticket-dashboard"),
]
