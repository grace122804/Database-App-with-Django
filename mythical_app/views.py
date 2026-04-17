from django.shortcuts import render
from .models import Patient


def patient_list(request):
    """
    Display a list of all patients with their owner and universe information.
    Uses select_related for efficient database queries.
    """
    patients = Patient.objects.select_related('owner', 'universe').all()
    return render(request, 'patients_list.html', {'patients': patients})
