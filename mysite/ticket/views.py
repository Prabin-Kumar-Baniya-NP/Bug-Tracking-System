from django.shortcuts import render, reverse
from ticket.forms import BugReportForm
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
        form = BugReportForm(request.user.id, request.POST)
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
    paginate_by = 2
    template_name = "ticket/submitted-tickets.html"

    def get_queryset(self):
        return Ticket.objects.filter(submitted_by = self.request.user)

@login_required
def reviewTickets(request):
    adminStatus = request.user.administratorStatus
    if True in adminStatus.values():
        ticket_list = Ticket.objects.filter(product_name = request.user.product_assigned.name, ticket_status = "SUB")
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