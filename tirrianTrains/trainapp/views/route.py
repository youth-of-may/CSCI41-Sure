from django.shortcuts import render
from trainapp.services.station_sql import *
from trainapp.services.route_sql import *
from trainapp.services.price_history_sql import *
from django.http import HttpResponse


def stations_list(request):
    context = {
        'local_station': list_stations(True),
        'intertown_station': list_stations(False),
    }
    return render(request, "trainapp/stations/station_list.html", context)

def station_detail(request, destinationID):
    context = {
        'station_name': get_station_name(destinationID),
        'routes': get_destination_routes(destinationID),
    }
    return render(request, "trainapp/stations/station_detail.html", context)

def station_price_history(request, routeID):
    ''' Show the price changes made on a specific route '''
    if request.method == 'POST':
        # Will insert logic to allow price change later on
        return(HttpResponse("<h1>Under Progress hehe</h1>"))
    else:
        return render(request, "trainapp/price_history.html",{'routePriceHistory':generate_price_history(routeID)})

# Unsure if I'll use this or not pa
def total_price_history(request):
    ''' Generate a full list of all changes to price across all stations '''
    return render(request, "trainapp/stations/station_detail.html", {'routePriceHistory':full_price_history()})