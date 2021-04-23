from django.shortcuts import render, reverse
from ticket.forms import BugReportForm, TicketUpdationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from ticket.models import Ticket
from company.models import Company
from product.models import Product
from team.models import Team
from designation.models import Designation
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def report_bug(request):
    if request.method == "POST":
        form = BugReportForm(request.user.id, request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Bug Reported Successfully")
            return HttpResponseRedirect(reverse("user:dashboard"))
        else:
            messages.error(request, "Please enter valid data")
            return HttpResponseRedirect(reverse("ticket:report-bug"))
    else:
        context = {
            'form': BugReportForm(request.user.id),
        }
        return render(request, "ticket/report-bug.html", context)


class SubmittedTicketsListView(LoginRequiredMixin, generic.ListView):
    model = Ticket
    paginate_by = 10
    template_name = "ticket/submitted-tickets.html"

    def get_queryset(self):
        return Ticket.objects.filter(submitted_by = self.request.user)

@login_required
def reviewTickets(request):
    adminStatus = request.user.administratorStatus
    if True in adminStatus.values():
        user_assigned_product = [product.id for product in request.user.product_assigned.all()]
        user_admin_product = [product.id for product in Product.objects.filter(administrator = request.user)]
        ticket_list = Ticket.objects.filter(product_name__in = user_admin_product + user_assigned_product, ticket_status = "SUB")
        paginator = Paginator(ticket_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj
        }
        return render(request, "ticket/review-tickets.html", context)
    else:
        messages.error(request, "You are not eligible to view this page")
        return HttpResponseRedirect(reverse("user:dashboard"))

class TicketDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ticket
    template_name = "ticket/details.html"

@login_required
def ticketUpdation(request, ticket_id):
    adminStatus = request.user.administratorStatus
    if True in adminStatus.values():
        if request.method == "POST":
            form = TicketUpdationForm(request.user.id,request.POST, files = request.FILES, instance = Ticket.objects.get(id = ticket_id))
            if form.is_valid():
                form.save()
                messages.success(request, "Ticket Details Updated Successfully")
                return HttpResponseRedirect(reverse("ticket:ticket-details",args = [ticket_id]))
            else:
                messages.error(request, "Please enter valid data. Try again")
                return HttpResponseRedirect(reverse("ticket:ticket-details",args = [ticket_id]))
        else:
            context = {
                'form' : TicketUpdationForm(request.user.id, instance = Ticket.objects.get(id = ticket_id)),
            }
            return render(request, "ticket/update-ticket.html", context)
    else:
        messages.error(request, "You are not eligible to view this page")
        return HttpResponseRedirect(reverse("user:dashboard"))

class AssignedTicketsListView(LoginRequiredMixin, generic.ListView):
    model = Ticket
    paginate_by = 10
    template_name = "ticket/assigned-tickets.html"

    def get_queryset(self):
        return Ticket.objects.filter(assigned_to = self.request.user)

class AssignedTicketDashboardDetailView(LoginRequiredMixin, generic.ListView):
    model = Ticket
    template_name = "ticket/ticket-dashboard.html"
    context_object_name = 'ticket'

    def get_queryset(self):
        return Ticket.objects.get(id = self.kwargs['pk'], assigned_to = self.request.user)