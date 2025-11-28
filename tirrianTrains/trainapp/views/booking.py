from django.shortcuts import render, redirect
from django.http import HttpResponse
from trainapp.services.booking_sql import list_local_trips, list_intertown_trips, get_trips
from trainapp.services.customer_sql import get_full_customer
from trainapp.services.ticket_sql import *
from datetime import date


def booking_page(request):
    ''' Shows all available bookings, separated into local and inter-town '''
    local_trips = list_local_trips()
    intertown_trips = list_intertown_trips()

    # Currently does not actually load the trips since the template is showing hardcoded stuff
    return render(request, "trainapp/booking/booking.html", {
        "local": local_trips,
        "intertown": intertown_trips,
    })
    
def booking_add(request, tripID):
    """
    Add or remove a trip to a potential ticket
    """
    
    customer_id = request.session.get("customer_id")
    if not customer_id:
        return redirect("login")
    
    customer = get_full_customer(customer_id)
    sessionTrips = request.session.get('selected_trips', [])
    
    if tripID not in sessionTrips:
        sessionTrips.append(tripID)
        request.session['selected_trips'] = sessionTrips
    else:
        sessionTrips.remove(tripID)
        request.session['selected_trips'] = sessionTrips
    
    # If removed all trips from session go back to booking
    if not sessionTrips:
        return redirect("booking_page")
    
    
    trips = get_trips(sessionTrips)
    context = {
        "customer": customer[0],
        "trips": trips,
        "selected_trips": sessionTrips,
    }
    
    return render(request, "trainapp/booking/ticket_preview.html", context)

def create_ticket(request):
    """
    Creates new ticket, ticketTrips and then shows the final ticket
    Clears tripIDs from session
    """
    customer_id = request.session.get("customer_id")
    if not customer_id:
        return redirect("login")
    
    # Get all necessary data to make the final ticket and trips
    sessionTrips = request.session.get('selected_trips', [])
    trips = get_trips(sessionTrips)
    totalCost = sum(t['baseCost'] for t in trips)
    
    ticketID = db_create_ticket(customer_id, date.today(), totalCost)
    # Create all the individual trips
    for x in range(len(trips)):
        create_ticket_trip(ticketID, sessionTrips[x], trips[x]["baseCost"])
    
    # Clear session cookies then redirect
    del request.session['selected_trips']
    return redirect("ticket_trips", pk=ticketID)