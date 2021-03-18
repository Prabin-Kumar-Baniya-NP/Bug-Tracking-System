from django.shortcuts import render, reverse
from team.forms import TeamCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


@login_required
def teamCreationView(request):
    if request.method == "POST":
        form = TeamCreationForm(request.user.id, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Team Added Successfully")
            return HttpResponseRedirect(reverse("user:dashboard"))
    else:
        context = {
            'form': TeamCreationForm(request.user.id),
        }
        return render(request,  "team/team-creation-page.html", context)
