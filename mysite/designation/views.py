from django.shortcuts import render, reverse
from designation.forms import DesignationCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


@login_required
def designationCreationView(request):
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
