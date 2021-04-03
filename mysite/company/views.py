from django.shortcuts import render, reverse
from company.forms import CompanyCreationForm, CompanyUpdationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic 
from company.models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def companyCreationView(request):
    if request.method == "POST":
        form = CompanyCreationForm(request.user.id, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Company Created Successfully")
            return HttpResponseRedirect(reverse("user:dashboard"))
        else:
            messages.error(request, "Please enter valid data")
            return HttpResponseRedirect(reverse("user:dashboard"))
    else:
        context = {
            'form': CompanyCreationForm(request.user.id),
        }
        return render(request,  "company/company-creation-page.html", context)

class CompanyListView(LoginRequiredMixin, generic.ListView):
    model = Company
    template_name = "company/index.html"

    def get_queryset(self):
        try:
            user_associated_company_id = self.request.user.company_associated.id
            return Company.objects.filter(administrator = self.request.user.id).union(Company.objects.filter(id = user_associated_company_id))
        except:
            return Company.objects.filter(administrator = self.request.user)

class CompanyDetailView(LoginRequiredMixin, generic.DetailView):
    model = Company
    template_name = "company/details.html"

@login_required
def companyUpdationView(request, company_id):
    requested_company = Company.objects.get(id = company_id)
    if request.user in requested_company.administrator.all():
        if request.method == "POST":
            form = CompanyUpdationForm(company_id, request.POST, instance = requested_company)
            if request.user in requested_company.administrator.all():
                if form.is_valid():
                    form.save()
                    messages.success(request, "Company Details Updated Successfully")
                    return HttpResponseRedirect(reverse("user:dashboard"))
                else:
                    messages.error(request, "Please enter valid data")
                    return HttpResponseRedirect(reverse("user:dashboard"))
            else:
                messages.error(request, "You dont have permissions to update the company details")
                return HttpResponseRedirect(reverse("user:dashboard"))
        else:
            context = {
                'form': CompanyUpdationForm(company_id, instance = requested_company),
            }
            return render(request,  "company/company-updation-page.html", context)
    else:
        messages.error(request, "You are not eligible to update the company details")
        return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def companyDeletionView(request, company_id):
    requested_company = Company.objects.get(id = company_id)
    if request.user in requested_company.administrator.all():
        requested_company.delete()
        messages.success(request, "Company deleted successfully")
        return HttpResponseRedirect(reverse("user:dashboard"))
    else:
        messages.error(request, "You are not eligible to delete the company details")
        return HttpResponseRedirect(reverse("user:dashboard"))