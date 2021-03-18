from django.shortcuts import render, reverse
from company.forms import CompanyCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


@login_required
def companyCreationView(request):
    if request.method == "POST":
        form = CompanyCreationForm(request.user.id, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Company Created Successfully")
            return HttpResponseRedirect(reverse("user:dashboard"))
    else:
        context = {
            'form': CompanyCreationForm(request.user.id),
        }
        return render(request,  "company/company-creation-page.html", context)
