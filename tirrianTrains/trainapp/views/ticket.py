from django.shortcuts import render
from django.http import HttpResponse
from trainapp.services.customer_sql import get_customer
from trainapp.services.ticket_sql import ticketDetails

def ticket_preview(request):
    ''' Shows the customer details that will be added to the train ticket and the trip itinerary '''
    if request.method == "POST":
        return HttpResponse("TODO add trip or confirm ticket logic")
    else:
        # Will add logic to get the customer ID instead of hard coded
        customer = get_customer(1)
        ticket = ticketDetails()
        
        return render(request, "ticket_preview.html", {
            "customer": customer,
            "ticket": ticket,
        })