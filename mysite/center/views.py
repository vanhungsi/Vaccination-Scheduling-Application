from django.shortcuts import render
from django.urls import reverse

from .models import Center
from .forms import CenterForm
from django.http import HttpResponseRedirect, Http404


def center_list(request):
    objects = Center.objects.all()
    context = {
        'center': objects,
    }
    return render(request, 'center/center-list.html', context)


def center_detail(request, id):
    object = Center.objects.get(id=id)
    context = {
        'center': object,
    }
    return render(request, 'center/center-detail.html', context)


def create_center(request):
    if request.method == 'POST':
        form = CenterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("center:list"))
        return render(request, 'center/create-center.html', {"form": form})
    # GET
    context = {
        'form': CenterForm()
    }
    return render(request, 'center/create-center.html', context)

def update_center(request, id):
    try:
        center = Center.objects.get(id=id)
    except Center.DoesNotExist:
        raise Http404("Center not found")

    if request.method == 'POST':
        form = CenterForm(request.POST, instance=center)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("center:detail", kwargs={"id": center.id}))
        return render(request, 'center/update-center.html', {'form':form})
    # Get
    context = {
        "form": CenterForm(instance = center)
    }
    return render( request, 'center/update-center.html', context)

def delete_center(request, id):
    try:
        center = Center.objects.get(id=id)
    except Center.DoesNotExist:
        raise Http404("Center not found")
    if request.method == 'POST':
        center.delete()
        return HttpResponseRedirect(reverse("center:list"))

    context = {
        'center': center
    }
    return render(request, 'center/delete-center.html', context)