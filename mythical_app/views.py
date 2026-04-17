from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.shortcuts import render

from .models import Owner, Patient


def patient_list(request):
    """
    Display a list of all patients with their owner and universe information.
    Uses select_related for efficient database queries.
    """
    patients = Patient.objects.select_related('owner', 'universe').all()
    return render(request, 'patients_list.html', {'patients': patients})


class OwnerListView(ListView):
    model = Owner
    context_object_name = 'owners'
    template_name = 'mythical_app/owner_list.html'
    paginate_by = 20


class OwnerCreateView(CreateView):
    model = Owner
    fields = ['name', 'phone', 'email', 'address', 'universe']
    template_name = 'mythical_app/owner_form.html'
    success_url = reverse_lazy('owner_list')


class OwnerUpdateView(UpdateView):
    model = Owner
    fields = ['name', 'phone', 'email', 'address', 'universe']
    template_name = 'mythical_app/owner_form.html'
    success_url = reverse_lazy('owner_list')


class OwnerDeleteView(DeleteView):
    model = Owner
    template_name = 'mythical_app/owner_confirm_delete.html'
    success_url = reverse_lazy('owner_list')
