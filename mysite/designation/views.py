from django.shortcuts import render, reverse
from designation.forms import DesignationCreationForm, DesignationUpdationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from designation.models import Designation

@login_required
def designationCreationView(request):
    """
    This view handles the get and post method of request for Designation Creation Form
    """
    if request.method == "POST":
        form = DesignationCreationForm(request.user.id, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New Designation Added Successfully")
            return HttpResponseRedirect(reverse("user:dashboard"))
    else:
        context = {
            'form': DesignationCreationForm(request.user.id),
        }
        return render(request,  "designation/designation-creation-page.html", context)

class DesignationListView(LoginRequiredMixin, generic.ListView):
    """
    This view lists all the designations of the requested user.
    """
    model = Designation
    template_name = "designation/index.html"

    def get_queryset(self):
        user_assigned_designation = self.request.user.designation_assigned.all()
        return Designation.objects.filter(administrator = self.request.user.id).union(user_assigned_designation)

class DesignationDetailView(LoginRequiredMixin, generic.DetailView):
    """
    This view displays the details of the designation object reqested by the user
    Requires the pk of Designation Object.
    """
    model = Designation
    template_name = "designation/details.html"

@login_required
def designationUpdationView(request, designation_id):
    """
    This view handles the get and post method request of designation updation form.
    """
    requested_designation = Designation.objects.get(id = designation_id)
    if request.user in requested_designation.administrator.all():
        if request.method == "POST":
            form = DesignationUpdationForm(request.user.id, designation_id, request.POST, instance = requested_designation)
            if request.user in requested_designation.administrator.all():
                if form.is_valid():
                    form.save()
                    messages.success(request, "Designation Details Updated Successfully")
                    return HttpResponseRedirect(reverse("user:dashboard"))
                else:
                    messages.error(request, "Please enter valid data")
                    return HttpResponseRedirect(reverse("user:dashboard"))
            else:
                messages.error(request, "You dont have permissions to update the company details")
                return HttpResponseRedirect(reverse("user:dashboard"))
        else:
            context = {
                'form': DesignationUpdationForm(request.user.id,designation_id, instance = requested_designation),
            }
            return render(request,"designation/designation-updation-page.html", context)
    else:
        messages.error(request, "You are not eligible to update the designation details")
        return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def designationDeletionView(request, designation_id):
    """
    This view deletes the designation object requested by the user through designation_id
    """
    requested_designation = Designation.objects.get(id = designation_id)
    if request.user in requested_designation.administrator.all():
        requested_designation.delete()
        messages.success(request, "Designation deleted successfully")
        return HttpResponseRedirect(reverse("user:dashboard"))
    else:
        messages.error(request, "You are not eligible to delete the company details")
        return HttpResponseRedirect(reverse("user:dashboard"))
