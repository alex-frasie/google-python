from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm, ReviewForm


# Create your views here.

def product_create_view(request):
    form = RawProductForm()

    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect('/products')

    context = {
        'form': form
    }

    return render(request, "product/create.html", context)


def product_create_view2(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "product/create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'price': obj.price,
        'description': obj.description
    }
    return render(request, "product/detail.html", context)


def dynamic_lookup_view(request, prod_id):
    obj = get_object_or_404(Product, id=prod_id)

    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            obj.set_review(**form.cleaned_data)
            print(form.cleaned_data)
            obj.save()
            return redirect('/product/' + str(prod_id))

    context = {
        "object": obj,
        "form" : form
    }

    return render(request, "product/detail.html", context)


def product_delete_view(request, prod_id):
    obj = get_object_or_404(Product, id=prod_id)

    if request.method == "POST":
        obj.delete()
        return redirect('/products/')

    context = {
        "object": obj
    }

    return render(request, "product/delete.html", context)


def product_update_view(request, prod_id, new_review):
    obj = get_object_or_404(Product, id=prod_id)

    if request.method == "POST":
        obj.set_review(new_review)
        obj.save()
        return redirect('/products/')

    context = {
        "object": obj
    }

    return render(request, "product/detail.html", context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "product/list.html", context)
