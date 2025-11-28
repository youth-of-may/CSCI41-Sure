from django.shortcuts import render, redirect
from django.http import HttpResponse
from trainapp.services.booking_sql import list_local_trips, list_intertown_trips, get_trips
from trainapp.services.customer_sql import get_full_customer
import trainapp._db as db #importing to query sql directly in this view


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
    customer_id = request.session.get("customer_id")
    if not customer_id:
        return redirect("login")
    
    customer = get_full_customer(customer_id)
    print(customer)
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
    }
    print(context)
    
    return render(request, "trainapp/booking/ticket_preview.html", context)

def create_ticket(request, customerID):
    return HttpResponse("still making")