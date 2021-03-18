from django.shortcuts import render, reverse
from user.forms import UserCreationForm, UserUpdationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login as perform_login, logout as perform_logout, update_session_auth_hash
from user.models import User

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
                    return HttpResponseRedirect("/index/")
            else:
                messages.error(request, "Please enter valid data")
                return HttpResponseRedirect("/index/")
        else:
            context = {
                'form' : AuthenticationForm()
            }
            return render(request, "user/index.html", context)
    else:
        messages.success(request, "Already Logged In")
        return render(request, "user/dashboard.html", {})
    

def UserCreationView(request):
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

def logout(request):
    """
    This view will handle the logout of the user
    """
    perform_logout(request)
    messages.success(request, "Logged Out Successfully")
    return HttpResponseRedirect("/index/")

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
        return HttpResponseRedirect('/index/')

def profile_view(request):
    """
    This view will show the user personal and employee data
    """
    context = {
            "user_info" : User.objects.get(id = request.user.id),
    }
    return render(request, "user/profile-view.html", context)

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

def dashboard(request):
    return render(request, "user/dashboard.html", {})