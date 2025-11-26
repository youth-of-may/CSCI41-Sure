from django.shortcuts import render, redirect
from trainapp.services.maintenance_sql import *
from trainapp.services.customer_sql import *
from trainapp.services.ticket_sql import *

def admin_details(request):
    context = {
        'trains': list_trains(),
        'customers': list_customers(),
        'ticketDates': list_ticket_dates(),
    }
    return render(request, "trainapp/admin/admin_view.html", context)

def admin_travel_history(request, pk):
    context = {
        'customer': get_customer(pk),
        'travel_history': generate_travel_history(pk)
    }
    return render(request, "trainapp/admin/travel_history.html", context)

def admin_ticket_sales(request):
    """
    Show the sales from a specific date,
    -- Is called by the form in admin_details
    """
    date = request.GET.get("ticketDate")
    print("showing date: ", date)
    
    if date:
        sql = "SELECT * FROM ticket WHERE ticketDate = %s"
        tickets = db.execute(sql, [date])
    else:
        tickets = []
    
    print(tickets)
    
    context = {
        "tickets": tickets,
        "date": date,    
    }

    return render(request, "trainapp/admin/ticket_sales.html", context)

def customer_ticket_trips(request, pk):
    """Show trip and customer details given ticketID"""

    context= {
        'ticketNum': pk,
        'customer': ticketCustDetails(ticket_id=pk),
        'trips': ticketTripDetails(ticket_id=pk),
    }
    return render(request, "trainapp/admin/customer_ticket.html", context)