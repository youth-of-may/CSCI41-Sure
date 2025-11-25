from django.shortcuts import render, redirect
from trainapp.services.maintenance_sql import *
from trainapp.services.customer_sql import *
from trainapp.services.ticket_sql import *
from django.http import HttpResponse

def admin_details(request):
    context = {
        'trains': list_trains(),
        'customers': list_customers(),
        'tickets': list_tickets(),
    }
    return render(request, "trainapp/admin/admin_view.html", context)

def admin_travel_history(request, pk):
    context = {
        'customer': get_customer(pk),
        'travel_history': generate_travel_history(pk)
    }
    return render(request, "trainapp/admin/travel_history.html", context)

def admin_ticket_sales(request):
    return HttpResponse("still working")