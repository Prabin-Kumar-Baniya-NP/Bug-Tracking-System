from django.shortcuts import render, reverse
from user.forms import UserCreationForm, UserUpdationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login as perform_login, logout as perform_logout, update_session_auth_hash
from user.models import User
from company.models import Company
from product.models import Product
from team.models import Team
from designation.models import Designation
from django.contrib.auth.decorators import login_required
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from ticket.models import Ticket

def index(request):
    """
    This view will handle the signin process
    """
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request = request, data=request.POST)
            if form.is_valid():
                requested_username = form.cleaned_data["username"]
                requested_password = form.cleaned_data["password"]
                user = authenticate(username = requested_username, password = requested_password)
                if user is not None:
                    perform_login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return HttpResponseRedirect("/dashboard/")
                else:
                    messages.error(request, "Please enter valid username and password")
                    return HttpResponseRedirect(reverse("user:index"))
            else:
                messages.error(request, "Please enter valid data")
                return HttpResponseRedirect(reverse("user:index"))
        else:
            context = {
                'form' : AuthenticationForm()
            }
            return render(request, "user/index.html", context)
    else:
        messages.success(request, "Already Logged In")
        return render(request, "user/dashboard.html", {})
    

def UserCreationView(request, **kwargs):
    """
    This view will handle the user creation form
    """
    if request.method == "POST":
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            messages.success(request,"User Created Successfully")
            return HttpResponseRedirect(reverse("user:index"))
        else:
            messages.error(request, "Unable to create new user. Please enter valid data")
            return HttpResponseRedirect(reverse("user:sign-up"))
    else:
        context = {
            'form' : UserCreationForm()  
        }
        return render(request, "user/sign_up.html", context)

@login_required
def addCompanyToUserProfile(request,username,company_id):
    user = User.objects.get(username = username)
    user.company_associated = Company.objects.get(id = company_id)
    user.save()
    messages.success(request, f"{user} added under this company")
    return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def addProductToUserProfile(request,username, product_id):
    user = User.objects.get(username = username)
    product = Product.objects.get(id = product_id)
    user.company_associated = Company.objects.get(id = product.company.id)
    user.product_assigned.add(product)
    user.save()
    messages.success(request, f"{product} assigned to {user}")
    return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def addTeamToUserProfile(request,username, team_id):
    user = User.objects.get(username = username)
    team = Team.objects.get(id = team_id)
    product = Product.objects.get(id = team.product.id)
    user.company_associated = Company.objects.get(id = product.company.id)
    user.product_assigned.add(product)
    user.team_assigned.add(team)
    user.save()
    messages.success(request, f"{team} assigned to {user}")
    return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def addDesignationToUserProfile(request,username, designation_id):
    user = User.objects.get(username = username)
    designation = Designation.objects.get(id = designation_id)
    team = Team.objects.get(id = designation.team.id)
    product = Product.objects.get(id = team.product.id)
    user.company_associated = Company.objects.get(id = product.company.id)
    user.product_assigned.add(product)
    user.team_assigned.add(team)
    user.designation_assigned.add(designation)
    user.save()
    messages.success(request, f"{designation} assigned to {user}")
    return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def logout(request):
    """
    This view will handle the logout of the user
    """
    perform_logout(request)
    messages.success(request, "Logged Out Successfully")
    return HttpResponseRedirect(reverse("user:index"))

@login_required
def change_password(request):
    """
    This view will handle the changing of passsowrd of the user
    """
    if request.user.is_authenticated:
        form = PasswordChangeForm(user=request.user)
        if request.method == "POST":
            form= PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password Changed Successfully")
                return HttpResponseRedirect('/dashboard/')
            else:
                form = PasswordChangeForm(user=request.user)
                messages.error(request, "Please enter valid password")
                return HttpResponseRedirect(reverse("user:change-password"))
        else:
            form = PasswordChangeForm(user = request.user)
            return render(request, "user/change-password.html", {'form': form})
    else:
        messages.error(request, "You must login to change the password")
        return HttpResponseRedirect(reverse("user:index"))

@login_required
def profile_view(request):
    """
    This view will show the user personal and employee data
    """
    context = {
            "user_info" : User.objects.get(id = request.user.id),
    }
    return render(request, "user/profile-view.html", context)

@login_required
def update_profile(request):
    """
    This view will update the user informations
    """
    if request.method == "POST":
        updated_profile = UserUpdationForm(request.POST, instance = request.user)
        if updated_profile.is_valid():
            updated_profile.save()
            messages.success(request, "Profile Updated Successfully")
            return HttpResponseRedirect('/dashboard/')
    else:
        user = User.objects.get(id = request.user.id)
        context = {
            'user' : user,
            "form" : UserUpdationForm(instance = user),
        }
        return render(request, "user/update-profile.html", context)

@login_required
def dashboard(request):
    context = {
        'tickets_submitted_count' : Ticket.objects.filter(ticket_status = "SUB", submitted_by = request.user).count(),
        'tickets_rejected_count' : Ticket.objects.filter(ticket_status = "REJ", submitted_by = request.user).count(),
        'tickets_approved_count' : Ticket.objects.filter(ticket_status__contains = "A&", submitted_by = request.user).count(),
        'tickets_postponed_count' : Ticket.objects.filter(ticket_status = "POS", submitted_by = request.user).count(),
        'tickets_resolved_count' : Ticket.objects.filter(ticket_status = "RES", submitted_by = request.user).count(),
        'tickets_closed_count' : Ticket.objects.filter(ticket_status = "CLO", submitted_by = request.user).count(),
        'tickets_duplicate_count' : Ticket.objects.filter(ticket_status = "DUP", submitted_by = request.user).count(),
        'tickets_assigned_count': Ticket.objects.filter(assigned_to = request.user).count(),

    }
    return render(request, "user/dashboard.html", context)

@login_required
def companyUnassociatedUserProfile(request,company_id):
    company = Company.objects.get(id = company_id)
    if request.user in company.administrator.all():
        user_list =User.objects.filter(company_associated = None)
        paginator = Paginator(user_list, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'company_id': company_id,
            'page_obj': page_obj,
        }
        return render(request, "user/company-unassociated-user-list.html", context)
    else:
        messages.error(request, "You are not eligible to perform this action")
        return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def productUnassignedUserProfile(request,product_id):
    product = Product.objects.get(id = product_id)
    if request.user in product.administrator.all():
        user_list =User.objects.filter(company_associated = product.company).difference(User.objects.filter(product_assigned = product))
        paginator = Paginator(user_list, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'product_id': product_id,
            'page_obj': page_obj,
        }
        return render(request, "user/product-assign-user-list.html", context)
    else:
        messages.error(request, "You are not eligible to perform this action")
        return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def teamUnassignedUserProfile(request,team_id):
    team = Team.objects.get(id = team_id)
    if request.user in team.administrator.all():
        user_list = User.objects.filter(company_associated = team.product.company).difference(User.objects.filter(team_assigned = team))
        paginator = Paginator(user_list, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'team_id': team_id,
            'page_obj': page_obj,
        }
        return render(request, "user/team-assign-user-list.html", context)
    else:
        messages.error(request, "You are not eligible to perform this action")
        return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def designationUnassignedUserProfile(request,designation_id):
    designation = Designation.objects.get(id = designation_id)
    if request.user in designation.administrator.all():
        user_list = User.objects.filter(company_associated = designation.team.product.company).difference(User.objects.filter(designation_assigned = designation))
        paginator = Paginator(user_list, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'designation_id': designation_id,
           'page_obj': page_obj,
        }
        return render(request, "user/designation-assign-user-list.html", context)
    else:
        messages.error(request, "You are not eligible to perform this action")
        return HttpResponseRedirect(reverse("user:dashboard"))