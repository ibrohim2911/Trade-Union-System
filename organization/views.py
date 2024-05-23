from django.shortcuts import render, get_object_or_404
from .models import Organization

def dashboard(request):
    organization_data = get_object_or_404(Organization, id=1)

    users_number = organization_data.users.count()

    context = {
        'current_money': organization_data.money,
        'monthly_money': organization_data.monthly_money,
        'tel_number': organization_data.phone_number,
        'name_organization': organization_data.organization_name,
        'created_at': organization_data.created_at,
        'users_number': users_number
    }

    return render(request, 'dashboard.html', context)


def employees(request):
    return render(request, 'employees.html')