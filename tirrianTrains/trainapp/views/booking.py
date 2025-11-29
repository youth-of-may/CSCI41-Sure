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
    selected_trips = request.session.get('selected_trips', [])
    return render(request, "trainapp/booking/booking.html", {
        "local": local_trips,
        "intertown": intertown_trips,
        "selected_trips": selected_trips,
    })
    
def booking_add(request, tripID):
    customer_id = request.session.get("customer_id")
    if not customer_id:
        return redirect("login")

    customer = get_full_customer(customer_id)
    sessionTrips = request.session.get('selected_trips', [])

    # Add/remove trip selection
    if tripID not in sessionTrips:
        sessionTrips.append(tripID)
    else:
        sessionTrips.remove(tripID)

    request.session['selected_trips'] = sessionTrips

    # If no trips left, go back
    if not sessionTrips:
        return redirect("booking_page")

    trips = get_trips(sessionTrips)

    # TOTAL COST = sum of baseCost values from route
    totalCost = sum(t['baseCost'] for t in trips)

    context = {
        "customer": customer[0],
        "trips": trips,
        "selected_trips": sessionTrips,
        "date": date.today(),
        "totalCost": totalCost,
    }

    return render(request, "trainapp/booking/ticket_preview.html", context)


def create_ticket(request):
    customer_id = request.session.get("customer_id")
    if not customer_id:
        return redirect("login")

    sessionTrips = request.session.get('selected_trips', [])
    trips = get_trips(sessionTrips)

    # Compute total cost dynamically
    totalCost = sum(t['baseCost'] for t in trips)

    # Create ticket (ticket table has no totalCost column)
    ticketID = db_create_ticket(customer_id, date.today())

    # Create each ticketTrip entry
    for i, trip in enumerate(trips):
        create_ticket_trip(ticketID, sessionTrips[i], trip["baseCost"])

    # Clear session
    del request.session['selected_trips']

    return redirect("ticket_trips", pk=ticketID)
