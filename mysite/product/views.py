from django.shortcuts import render, reverse
from product.forms import ProductCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


@login_required
def productCreationView(request):
    if request.method == "POST":
        form = ProductCreationForm(request.user.id, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Added Successfully")
            return HttpResponseRedirect(reverse("user:dashboard"))
    else:
        context = {
            'form': ProductCreationForm(request.user.id),
        }
        return render(request,  "product/product-creation-page.html", context)
