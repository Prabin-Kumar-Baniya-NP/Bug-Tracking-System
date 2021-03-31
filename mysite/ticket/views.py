from django.shortcuts import render, reverse
from ticket.forms import BugReportForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
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