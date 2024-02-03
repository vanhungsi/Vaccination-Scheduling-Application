from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Vaccine
from .forms import VaccineForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect


# Create your views here.

class VaccineList(View):
    def get(self, request):
        vaccine_list = Vaccine.objects.all()
        context = {
            'object_list': vaccine_list
        }
        return render(request, 'vaccine/vaccine-list.html', context)


class VaccineDetail(View):
    def get(self, request, id):
        try:
            vaccine = Vaccine.objects.get(id=id)
        except Vaccine.DoesNotExist:
            raise Http404("Vaccine not found")

        context = {
            'object': vaccine,
        }
        return render(request, 'vaccine/vaccine-detail.html', context)


class CreateVaccine(View):
    form_class = VaccineForm
    template_name = 'vaccine/create-vaccine.html'

    def get(self, request):
        context = {
            'form': self.form_class()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vaccine:list'))
        return render(request, self.template_name, {'form': form})


class UpdateVaccine(View):
    form_class = VaccineForm
    template_name = 'vaccine/update-vaccine.html'

    def get(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        context = {
            'form': self.form_class(instance=vaccine),
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        form = self.form_class(request.POST, instance=vaccine)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vaccine:detail', kwargs={"id": vaccine.id}))
        return render(request, self.template_name, {'form': form})


class DeleteVaccine(View):
    template_name = 'vaccine/delete-vaccine.html'

    def get(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        context = {
            'object': vaccine
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        Vaccine.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('vaccine:list'))
