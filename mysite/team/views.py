from django.shortcuts import render, reverse
from team.forms import TeamCreationForm, TeamUpdationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from team.models import Team
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def teamCreationView(request):
    """
    This view handles the get and post request of Team Creation form.
    """
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

class TeamListView(LoginRequiredMixin, generic.ListView):
    """
    This view list the team objects associated with the user.
    """
    model = Team
    template_name = "team/index.html"

    def get_queryset(self):
        user_assigned_team = self.request.user.team_assigned.all()
        return Team.objects.filter(administrator = self.request.user.id).union(user_assigned_team)

class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    """
    This view provides the details of Team object
    Requires pk for Team for querying the database.
    """
    model = Team
    template_name = "team/details.html"

@login_required
def teamUpdationView(request, team_id):
    """
    This view handles the get and post method of request for Team Updation Form.
    """
    requested_team = Team.objects.get(id = team_id)
    if request.user in requested_team.administrator.all():
        if request.method == "POST":
            form = TeamUpdationForm(request.user.id, team_id, request.POST, instance = requested_team)
            if request.user in requested_team.administrator.all():
                if form.is_valid():
                    form.save()
                    messages.success(request, "Team Details Updated Successfully")
                    return HttpResponseRedirect(reverse("user:dashboard"))
                else:
                    messages.error(request, "Please enter valid data")
                    return HttpResponseRedirect(reverse("user:dashboard"))
            else:
                messages.error(request, "You dont have permissions to update the company details")
                return HttpResponseRedirect(reverse("user:dashboard"))
        else:
            context = {
                'form': TeamUpdationForm(request.user.id,team_id, instance = requested_team),
            }
            return render(request,"team/team-updation-page.html", context)
    else:
        messages.error(request, "You are not eligible to update the team details")
        return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def teamDeletionView(request, team_id):
    """
    This view deletes the team object
    Requires pk of Team for deletion.
    """
    requested_team = Team.objects.get(id = team_id)
    if request.user in requested_team.administrator.all():
        requested_team.delete()
        messages.success(request, "Team deleted successfully")
        return HttpResponseRedirect(reverse("user:dashboard"))
    else:
        messages.error(request, "You are not eligible to delete the company details")
        return HttpResponseRedirect(reverse("user:dashboard"))
