from django.shortcuts import render, reverse
from product.forms import ProductCreationForm, ProductUpdationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product

@login_required
def productCreationView(request):
    if request.method == "POST":
        form = ProductCreationForm(request.user.id, request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Added Successfully")
            return HttpResponseRedirect(reverse("user:dashboard"))
    else:
        context = {
            'form': ProductCreationForm(request.user.id),
        }
        return render(request,  "product/product-creation-page.html", context)

class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    template_name = "product/index.html"

    def get_queryset(self):
        user_assigned_product = self.request.user.product_assigned.all()
        return Product.objects.filter(administrator = self.request.user.id).union(user_assigned_product)

class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    template_name = "product/details.html"

@login_required
def productUpdationView(request, product_id):
    requested_product = Product.objects.get(id = product_id)
    if request.user in requested_product.administrator.all():
        if request.method == "POST":
            form = ProductUpdationForm(request.user.id, product_id, request.POST, files=request.FILES, instance = requested_product)
            if request.user in requested_product.administrator.all():
                if form.is_valid():
                    form.save()
                    messages.success(request, "Product Details Updated Successfully")
                    return HttpResponseRedirect(reverse("user:dashboard"))
                else:
                    messages.error(request, "Please enter valid data")
                    return HttpResponseRedirect(reverse("user:dashboard"))
            else:
                messages.error(request, "You dont have permissions to update the company details")
                return HttpResponseRedirect(reverse("user:dashboard"))
        else:
            context = {
                'form': ProductUpdationForm(request.user.id,product_id, instance = requested_product),
            }
            return render(request,"product/product-updation-page.html", context)
    else:
        messages.error(request, "You are not eligible to update the product details")
        return HttpResponseRedirect(reverse("user:dashboard"))

@login_required
def productDeletionView(request, product_id):
    requested_product = Product.objects.get(id = product_id)
    if request.user in requested_product.administrator.all():
        requested_product.delete()
        messages.success(request, "Product deleted successfully")
        return HttpResponseRedirect(reverse("user:dashboard"))
    else:
        messages.error(request, "You are not eligible to delete the company details")
        return HttpResponseRedirect(reverse("user:dashboard"))