from django.shortcuts import render
from trainapp.services.booking_sql import list_local_trips, list_intertown_trips

def booking_page(request):
    ''' Shows all available bookings, separated into local and inter-town '''
    local_trips = list_local_trips()
    intertown_trips = list_intertown_trips()
    
    # Currently does not actually load the trips since the template is showing hardcoded stuff
    return render(request, "trainapp/booking.html", {
        "local_trips": local_trips,
        "intertown_trips": intertown_trips,
    })