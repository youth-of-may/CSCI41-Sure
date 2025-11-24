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

def route_price_history(request, routeID):
    ''' Show the price changes made on a specific route '''
    return render(request, "trainapp/price/price_history.html",{'routePriceHistory':generate_price_history(routeID)})

def change_route_price(request, routeID, newPrice):
    ''' Change the base price of a route '''
    if request.method == 'POST':
        return HttpResponse("Work in Progress")
    else:
        sql = '''
        '''
        #TODO
        return render(request, "trainapp/price/price_change.html")