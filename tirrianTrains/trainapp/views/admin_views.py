from django.shortcuts import render, redirect
from trainapp.services.maintenance_sql import *
from trainapp.services.customer_sql import *

def admin_details(request):
    context = {
        'trains': list_trains(),
        'customers': list_customers(),
    }
    return render(request, "trainapp/admin_view.html", context)